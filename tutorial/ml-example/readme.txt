In the file "fake_tweet_sample.txt" you can find JSON that have the following format:

{
  "author_first_name": "John",
  "author_last_name": "Doe",
  "time": "10 October 2017",
  "tweet_content": "WOW this Narcos new season was awesome can't wait for season 4",
  "hashtags": "#narcos #netflix #amazing"
}

The goal is to transform those JSON into another format like:

{
  "name": "John Doe",
  "hashtags": ["#narcos", "#netflix", "#amazing"],
  "time": "10 October 2017",
  "created_at": "2017-09-04T08:39:54.897Z"
  "tweet_content": "WOW this Narcos new season was awesome can't wait for season 4",
  "sentiment": "positive"
}

You will have as well to build your "Machine Learning API" to generate the "sentiment"
field. Complete the file "sentiment_server.py" to do so.
