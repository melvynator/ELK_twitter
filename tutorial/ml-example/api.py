import pickle
from flask import Flask, jsonify, request
from elasticsearch import Elasticsearch

app = Flask(__name__)

es = Elasticsearch([{"host": "localhost", "port": 9200}])


@app.route('/predict', methods=['POST'])
def predict_a_tweet():
    # Load the Machine learning model based on labeled data
    vectorizer = pickle.load(open("vectorizer.p", 'rb'))
    classifier = pickle.load(open("classifier.p", 'rb'))
    # Retrieve the value of the tweet that is send through the POST
    # And put the value in a list
    tweet_content =
    # Vectorized into a TF-IDF vector the content of the tweet using
    # loaded vectorizer (Scikit learn)
    tfidf_to_predict =
    # Predict the sentiment of the tweet using the loaded classifier (SK learn)
    predicted =
    # Return the predicted value of the tweet
    return jsonify(response= )


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
