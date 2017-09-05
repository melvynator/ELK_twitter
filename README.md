# ELK for Twitter


This repo aim to provide a fully working out of the box data pipeline for Twitter using the ELK stack.

The presentation-example folder contains a fully working example that I use in the presentation of this pipeline: <insert link here later>, you can use it to play around and familiarize yourself with ELK.

You need to have installed ELasticsearch, Logstash and Kibana to use it.
You also need a twitter developer account.

Clone the repository:

`git clone https://github.com/melvynator/ELK_twitter.git`

Once you have downloaded the repository:

You have to write down your API keys in the file:

`ELK_twitter/twitter-ELK/config/twitter-pipeline.conf`

      consumer_key => "<YOUR-KEY>"
      consumer_secret => "<YOUR-KEY>"
      oauth_token => "<YOUR-KEY>"
      oauth_token_secret => "<YOUR-KEY>"


`cd ELK_twitter/twitter-ELK`


You have to change the 

First make sure that elasticsearch is started.



Then you can launch the pipeline with the following:

`logstash -f config/twitter-pipeline.conf`

