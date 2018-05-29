import ast
import os


def load(filepath=None):
    if filepath and os.path.exists(filepath):
        pass
    else:
        if not os.path.exists('.env'):
            return False
        filepath = os.path.join('.env')

    for key, value in _get_line_(filepath):
        os.environ[key] = str(value)
    return True


def _get_line_(filepath):
    for line in open(filepath):
        line = line.strip()

        if line.startswith('#') or '=' not in line:
            continue

        key, value = line.split('=', 1)

        key = key.strip().upper()
        value = value.strip()

        if not (key and value):
            continue

        try:
            value = ast.literal_eval(value)
        except (ValueError, SyntaxError):
            pass

        yield (key, value)


load('../.env')

TWITTER_CONSUMER_KEY = os.environ.get('TWITTER_CONSUMER_KEY')
TWITTER_CONSUMER_SECRET = os.environ.get('TWITTER_CONSUMER_SECRET')
TWITTER_ACCESS_TOKEN_KEY = os.environ.get('TWITTER_ACCESS_TOKEN_KEY')
TWITTER_ACCESS_TOKEN_SECRET = os.environ.get('TWITTER_ACCESS_TOKEN_SECRET')
