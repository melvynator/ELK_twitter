import pickle
from elasticsearch import Elasticsearch
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB


def get_term_vectors(es, document_field):
    delete_neutral_query = {
      "query": {
        "match": {
          "sentiment": "neutral"
        }
      }
    }
    es.delete_by_query(index="twitter", doc_type="tweet", body=delete_neutral_query)
    non_sentiment_tweet = {
      "query": {
        "bool": {
          "must_not":{
            "exists": {
              "field": "sentiment"
            }
          }
        }
      }
    }
    es.delete_by_query(index="twitter", doc_type="tweet", body=non_sentiment_tweet)
    query = {
      "_source": ["_id", "_parent", "sentiment"],
      "query": {
        "exists": {
          "field": "sentiment"
        }
      }
    }
    response = es.search(index="twitter", doc_type="tweet", body=query, size=200)
    tuples_parent_child = [(document["_parent"], document["_id"]) for document in response["hits"]["hits"]]
    targets = [document["_source"]["sentiment"] for document in response["hits"]["hits"]]
    documents = [{"_index": "twitter", "_type": "tweet", "_id": tuple_parent_child[1], "_parent": tuple_parent_child[0], "fields": [document_field]} for tuple_parent_child in tuples_parent_child]
    term_vectors_query = {"docs": documents}
    response = es.mtermvectors(body=term_vectors_query)
    strings_of_tokens = []
    for doc in response["docs"]:
        string_of_tokens = ""
        for key in doc["term_vectors"]["tweet_content.nlp"]["terms"]:
            string_of_tokens += key + " "
        strings_of_tokens.append(string_of_tokens)
    return strings_of_tokens, targets


def build_model(es):
    strings_of_tokens, targets = get_term_vectors(es, "tweet_content.nlp")
    vectorizer = TfidfVectorizer()
    training_tfidf = vectorizer.fit_transform(strings_of_tokens)
    classifier = MultinomialNB().fit(training_tfidf, targets)
    pickle.dump(classifier, open("../models/classifier.p", 'wb'))
    pickle.dump(vectorizer, open("../models/vectorizer.p", 'wb'))


es = Elasticsearch([{"host": "localhost", "port": 9200}])
build_model(es)
