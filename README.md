# ELK for Twitter sentiment analysis


## Contributing

This repository is fully free and fully open source. The license is Apache 2.0, meaning you are pretty much free to use it however you want in whatever way.

All contributions are welcome: ideas, pull requests, issues, documentation improvement, complaints.


## Summary

#### [+ Introduction](#introduction)
#### [+ Getting started](#getting-started)
#### [+ Requirements](#requirements)
#### [+ Ressources](#ressources)





## Introduction

This repository aims to provide a fully working "out-of-the-box" data pipeline for doing Machine learning on Twitter data using the ELK (Elasticsearch, Logstash, and Kibana) stack.

After having installed ELK you should be able in 5 minutes to visualize dashboard like the following:

<p align="center">
   <img src ="https://github.com/melvynator/ELK_twitter/blob/master/img/dashboard_visualization.gif" />
</p>

The offered pipeline can be modelized by the following flow chart:

![alt text](https://github.com/melvynator/ELK_twitter/blob/master/img/pipeline.png "Pipeline")

Let's have a look to the different part that are covered by this pipeline:

### Concerning the Logstash part

___

#### Input

The input used is Twitter, you can use it to track users or keywords or tweets in a specific location.

#### Filter

A lot of filters are applied and they are in charge of the following tasks:

* Remove depreciated field
* Divide the tweet in two or three events (users and tweet)
* Flatten the JSON
* Remove the fields not used

#### Output

Two output are defined:

* Elasticsearch: To allow a better search of your data
* MongoDB: To store your data

### Concerning the Elasticsearch part
____

#### Mapping

A mapping is provided and offers the following:

* A parent/child relationship between the tweet author and their tweets
* On text fields (Tweet content, User description, User location):
  * 3 Analyzers
  * Storing of the term vectors (For the 3 analyzers)
  * Storing of the token numbers (For the 3 analyzers)
* One geofield to locate the provenance of the tweet (if available)
* Many "keyword", "integer" field to all allow data filtering

The 3 analyzers are:
1. Standard
1. English
1. A custom analyzer that keeps emoticons and punctuations, which is useful for sentimental and emotion analysis

The mapping is not dynamic, Twitter having a lot of fields that are not (or poorly) documented, it avoid data polution and keep only the wanted data.

### Concerning the Kibana part
____

On Kibana side the repository offer:

* A dashboard for general data visualization
* A dashboard for comparison between a positive and negative tweet
* Different kind of visualizations

### Machine learning
____

A small "API" has been created to give you an idea about how you can use Logstash in order to "label" your tweet on the fly before indexation. The model is a dummy model but you can easily introduce your own complex model on the form of an API.

## Requirements

For the pipeline to work, you need a Twitter developer account, which you can obtain here: https://dev.twitter.com/resources/signup

### Linux users

This guide assumes that you have already installed [Elasticsearch](https://www.elastic.co/guide/en/elasticsearch/reference/current/setup.html), [Logstash](https://www.elastic.co/guide/en/logstash/current/installing-logstash.html) and [Kibana](https://www.elastic.co/guide/en/kibana/current/install.html). All three need to be installed properly in order to use this pipeline.

Once having installed ELK, here are some instructions to configure Elasticsearch to start automatically when the system boots up.

      sudo /bin/systemctl daemon-reload
      sudo /bin/systemctl enable elasticsearch.service

Elasticsearch can be started and stopped as follows:

      sudo systemctl start elasticsearch.service
      sudo systemctl stop elasticsearch.service

(Note that the same steps can be used for Kibana and Logstash)

### Mac users

```
brew install elasticsearch
brew install logstash
brew install kibana
```

## Getting started

Clone the repository:

`git clone https://github.com/melvynator/ELK_twitter.git`

### Setting up Elasticsearch
____

Make sure that you don't have an index `twitter` already present.

### Setting up your Machine Learning API
____

**If you don't have the need to make any API call you can skip this part**


Go into the main repository and create a virtual environement:

    cd ELK_twitter
    virtualenv -p python3 venv
    source venv/bin/activate

Then install Flask and Scikit-Learn (For the machine learning)

`pip install -r requirements.txt`

Then you can launch your local server:

    cd src/sentiment_service/
    python sentiment_server.py

### Setting up Logstash
___

To start configuring your logstash you have to open the configuration file:

`ELK_twitter/src/twitter-pipeline/config/twitter-pipeline.conf`

Replace the `<YOUR-KEY>` by your corresponding twitter key:


      consumer_key => "<YOUR-KEY>"
      consumer_secret => "<YOUR-KEY>"
      oauth_token => "<YOUR-KEY>"
      oauth_token_secret => "<YOUR-KEY>"

Now go into `twitter-pipeline`:

`cd ../src/twitter-pipeline`

Make sure that Elasticsearch is started and run on the port `9200`.

In addition, you also have to manually install the following plugins for Logstash:

**If you don't have the need to make any API call you don't have to install the REST Plugin**

**If you don't want to use mongoDB you don't have to install the MongoDB Plugin**

1. [MongoDB](https://github.com/logstash-plugins/logstash-output-mongodb) for Logstash (Allow you to store your data into mongoDB)
`sudo /usr/share/logstash/bin/logstash-plugin install logstash-filter-rest`
2. [REST](https://github.com/lucashenning/logstash-filter-rest) for Logstash (Allow you to make API call)
`sudo /usr/share/logstash/bin/logstash-plugin install logstash-output-mongodb`

**By default, the pipeline is only configured to output to Elasticsearch**, but if you have MongoDB installed, then you can uncomment the mongo output in the config file:
`ELK_twitter/src/twitter-pipeline/config/twitter-pipeline.conf`

**By default, the pipeline is configured to make API call**, but if you don't have any API you can remove the `rest` filter in the config file:
`ELK_twitter/src/twitter-pipeline/config/twitter-pipeline.conf`

Then, you can run the pipeline using:

`sudo /usr/share/logstash/bin/logstash -f config/twitter-pipeline.conf`

Or define logstash in your `SYSTEM_PATH` and run the following:

`logstash -f config/twitter-pipeline.conf`

You should see some logs that end up with:

`Successfully started Logstash sentiment_service endpoint {:port=>9600}`

### Setting up Kibana
___

Now go to Kibana: http://localhost:5601/

*Management => Index Patterns => Create Index Pattern*

Into the text box `Index name or pattern` type: `twitter`

Into the drop down box `Time Filter field name` choose: `inserted_in_es_at`

Click on create

Now go to:

*Management => Saved Objects => import*

And select the file in:

`ELK_twitter/src/twitter-pipeline/kibana-visualization/kibana_charts.json`

You can now go to *Dashboard*

This gif summarize the different step if you are lost.

![alt text](https://github.com/melvynator/ELK_twitter/blob/master/img/kibana_config.gif "Summary")



## Ressources

Thanks to stackoverflow community and Elastic community for the answer provided.

https://www.elastic.co/guide/en/logstash/current/introduction.html
https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html
