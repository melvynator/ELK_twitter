# ELK for Twitter

## Introduction

This repository aim to provide a fully working out of the box data pipeline for Twitter using the ELK stack.

The presentation-example folder contains a fully working example that I use in the presentation of this pipeline: <insert link here later>, you can use it to play around and familiarize yourself with ELK.

## Requirements

You need to have installed [Elasticsearch](https://www.elastic.co/guide/en/elasticsearch/reference/current/setup.html), [Logstash](https://www.elastic.co/guide/en/logstash/current/installing-logstash.html) and [Kibana](https://www.elastic.co/guide/en/kibana/current/install.html) to use this pipeline. 

Configuring Elasticsearch to start automatically when the system boots up.

      sudo /bin/systemctl daemon-reload
      sudo /bin/systemctl enable elasticsearch.service

Elasticsearch can be started and stopped as follows:

      sudo systemctl start elasticsearch.service
      sudo systemctl stop elasticsearch.service

You also need a twitter developer account => https://dev.twitter.com/resources/signup

## Getting started

Clone the repository:

`git clone https://github.com/melvynator/ELK_twitter.git`

Once you have downloaded the repository open the file:

`ELK_twitter/twitter-pipeline/config/twitter-pipeline.conf`

Replace the `<YOUR-KEY>` by your corresponding twitter key:


      consumer_key => "<YOUR-KEY>"
      consumer_secret => "<YOUR-KEY>"
      oauth_token => "<YOUR-KEY>"
      oauth_token_secret => "<YOUR-KEY>"


Now go into `twitter-pipeline`:

`cd ELK_twitter/twitter-pipeline`

Make sure that elasticsearch is started and run on the port 9600.

You can run the pipeline using:

`sudo /usr/share/logstash/bin/logstash -f config/twitter-pipeline.conf`

Or define logstash in your `SYSTEM_PATH` and run the following:

`logstash -f config/twitter-pipeline.conf`

You should see some logs that end up with:

`Successfully started Logstash API endpoint {:port=>9600}`

Now go to kibana: http://localhost:5601/

Management => Index Patterns => Create Index Pattern

Into the text box `Index name or pattern` type:

`twitter`

Into the drop down box `Time Filter field name` choose:

`inserted_in_es_at`

Click on create.

Now go into

Management => Saved Objects => import

And select the file in: 

`ELK_twitter/twitter-pipeline/kibana-visualization/kibana_charts.json`

You can now go into the "Dashboard" and you should see charts.
