from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from flask import Flask
from flask import jsonify,request
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

analyser = SentimentIntensityAnalyzer()

@app.route('/reviewAnalyser', methods =['POST'])
def sentiment_analyzer_scores():
    sentence = request.json['review']
    score = analyser.polarity_scores(sentence)
    print("{}".format(str(score)))
    print(score['compound'])
    if score['compound']<= 0.5:
        return jsonify({'Status': 'Success', 'result': 'negative'})
        # print("negative Review")
    else :
        return jsonify({'Status': 'Success', 'result': 'positive'})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
