from flask import Flask, request, jsonify, make_response, current_app
from twitter_handler import TwitterHandler
from datetime import timedelta
from functools import update_wrapper


def crossdomain(origin=None, methods=None, headers=None,
                max_age=21600, attach_to_all=True,
                automatic_options=True):
    if methods is not None:
        methods = ', '.join(sorted(x.upper() for x in methods))
    if headers is not None and not isinstance(headers, str):
        headers = ', '.join(x.upper() for x in headers)
    if not isinstance(origin, str):
        origin = ', '.join(origin)
    if isinstance(max_age, timedelta):
        max_age = max_age.total_seconds()

    def get_methods():
        if methods is not None:
            return methods

        options_resp = current_app.make_default_options_response()
        return options_resp.headers['allow']

    def decorator(f):
        def wrapped_function(*args, **kwargs):
            if automatic_options and request.method == 'OPTIONS':
                resp = current_app.make_default_options_response()
            else:
                resp = make_response(f(*args, **kwargs))
            if not attach_to_all and request.method != 'OPTIONS':
                return resp

            h = resp.headers

            h['Access-Control-Allow-Origin'] = origin
            h['Access-Control-Allow-Methods'] = get_methods()
            h['Access-Control-Max-Age'] = str(max_age)
            if headers is not None:
                h['Access-Control-Allow-Headers'] = headers
            return resp

        f.provide_automatic_options = False
        return update_wrapper(wrapped_function, f)
    return decorator


app = Flask(__name__)

@app.route('/hardmob_promos/', defaults={'item': None}, methods=['GET',])
@app.route('/hardmob_promos/<item>', methods=['GET',])
@crossdomain(origin='*')
def get_promos_hardmob(item):
    code, promo_tweets = 204, None

    if item:
        item = item.lower().strip()

    try:
        twitter_handler = TwitterHandler()
        promo_tweets = twitter_handler.fetch_hardmob_promos(item)

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
    from sys import argv
    app.run(debug=True, port=int(argv[1]) if len(argv) > 1 else 5000)
