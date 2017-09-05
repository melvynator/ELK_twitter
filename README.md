# ELK for Twitter

## Introduction

This repository aim to provide a fully working out of the box data pipeline for Twitter using the ELK stack.

The presentation-example folder contains a fully working example that I use in the presentation of this pipeline: <insert link here later>, you can use it to play around and familiarize yourself with ELK.

## Requirements

You need to have installed ELasticsearch, Logstash and Kibana to use this pipeline.

You also need a twitter developer account.

## Getting started

Clone the repository:

`git clone https://github.com/melvynator/ELK_twitter.git`

Once you have downloaded the repository open the file:

`ELK_twitter/twitter-ELK/config/twitter-pipeline.conf`

And replace the "<YOUR-KEY>" by your corresponding twitter key.

`
consumer_key => "<YOUR-KEY>"
consumer_secret => "<YOUR-KEY>"
oauth_token => "<YOUR-KEY>"
oauth_token_secret => "<YOUR-KEY>"
`

Now go into `twitter-ELK`:

`cd ELK_twitter/twitter-ELK`

Make sure that elasticsearch is started then you can launch the tweet collection with the following:

`logstash -f config/twitter-pipeline.conf`
