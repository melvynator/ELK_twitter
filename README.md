# ELK for Twitter sentiment analysis



## Summary

# [Introduction](#introduction)
# [Getting started](#getting-started)
# [Tutorial](#tutorial)
# [Ressources](#ressources)





## Introduction

This repository aims to provide a fully working "out-of-the-box" data pipeline for Twitter using the ELK (Elasticsearch, Logstash, and Kibana) stack. 

The `presentation-example` folder contains a fully working example that I use in the presentation of this pipeline: ~insert_link here later~, you can use it to play around and familiarize yourself with the ELK stack.


After having installed ELK you should be able in 5 minutes to visualize dashboard like the following:

<p align="center">
   <img src ="https://github.com/melvynator/ELK_twitter/blob/master/img/dashboard_visualization.gif" />
</p>

The offered pipeline can be modelized by the following flow chart:

![alt text](https://github.com/melvynator/ELK_twitter/blob/master/img/pipeline.png "Pipeline")

Let's have a look to the different part that are covered by this pipeline:

### Concerning the Logstash part

#### Input

The input used is Twitter, you can use it to track user or keyword or tweet in a specific location.

#### Filter

A lot of filters are applied and mainly do the following tasks:

* Remove depreciated field
* Divide the tweet in two or three events (users and tweet)
* Flatten the JSON
* Remove the fields not used

#### Output

Two output are defined:

* Elasticsearch: To allow a better search of your data
* MongoDB: To store your data

### Concerning the Elasticsearch part

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

On Kibana side the repository offer:

* A dashboard
* Different kind of visualizations

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

Make sure that you don't have an index `twitter` already present.

### Setting up Logstash

Once you have downloaded the repository, open the file:

`ELK_twitter/twitter-pipeline/config/twitter-pipeline.conf`

Replace the `<YOUR-KEY>` by your corresponding twitter key:


      consumer_key => "<YOUR-KEY>"
      consumer_secret => "<YOUR-KEY>"
      oauth_token => "<YOUR-KEY>"
      oauth_token_secret => "<YOUR-KEY>"


Now go into `twitter-pipeline`:

`cd ELK_twitter/twitter-pipeline`

Make sure that elasticsearch is started and run on the port `9600`.

You can run the pipeline using:

`sudo /usr/share/logstash/bin/logstash -f config/twitter-pipeline.conf`

Or define logstash in your `SYSTEM_PATH` and run the following:

`logstash -f config/twitter-pipeline.conf`

You should see some logs that end up with:

`Successfully started Logstash sentiment_service endpoint {:port=>9600}`

### Setting up Kibana

Now go to Kibana: http://localhost:5601/

*Management => Index Patterns => Create Index Pattern*

![alt text](https://github.com/melvynator/ELK_twitter/blob/master/img/management.png "Management")

![alt text](https://github.com/melvynator/ELK_twitter/blob/master/img/index_patterns.png "Index Patterns")

![alt text](https://github.com/melvynator/ELK_twitter/blob/master/img/conf_index_pattern.png "Config index")

Into the text box `Index name or pattern` type: `twitter`

Into the drop down box `Time Filter field name` choose: `inserted_in_es_at`

Click on create

![alt text](https://github.com/melvynator/ELK_twitter/blob/master/img/filled_index_pattern.png "Fill out")

Now go to:

*Management => Saved Objects => import*

![alt text](https://github.com/melvynator/ELK_twitter/blob/master/img/management.png "Management")

![alt text](https://github.com/melvynator/ELK_twitter/blob/master/img/saved_objects.png "Saved objects")

![alt text](https://github.com/melvynator/ELK_twitter/blob/master/img/import.png "Import")

And select the file in:

`ELK_twitter/twitter-pipeline/kibana-visualization/kibana_charts.json`

You can now go to *Dashboard*

![alt text](https://github.com/melvynator/ELK_twitter/blob/master/img/dashboard.png "Dashboard")

## Tutorial


## Ressources

Thanks to stackoverflow community and Elastic community for the answer provided.

https://www.elastic.co/guide/en/logstash/current/introduction.html
https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html

