from flask import Flask, jsonify

from utils.twitter_handler import TwitterHandler


app = Flask(__name__)


@app.route('/promos/', defaults={'text': None}, methods=['GET',])
@app.route('/promos/<text>', methods=['GET',])
def get_promos_hardmob(text):
    code, promo_tweets = 204, None

    if text:
        text = text.lower().strip()

    try:
        twitter = TwitterHandler()
        promo_tweets = twitter.fetch_hardmob_promos(text)

        if promo_tweets:
            code = 200

    except Exception as e:
        code = 404
        promo_tweets = e

    return jsonify(
        promos = promo_tweets,
        code = code
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
