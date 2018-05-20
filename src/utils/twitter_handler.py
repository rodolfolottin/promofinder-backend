from datetime import datetime

import twitter

import .settings


class TwitterHandler(object):
    def __init__(self):
        self.api = twitter.Api(
            consumer_key=settings.CONSUMER_KEY,
            consumer_secret=settings.CONSUMER_SECRET,
            access_token_key=settings.ACCESS_TOKEN_KEY,
            access_token_secret=settings.ACCESS_TOKEN_SECRET
        )

    def fetch_hardmob_promos(self, item_match=None):
        """
        Fetches hardmob sale's tweets and, if item_match given, returns only the ones with the item's text
        :param item_match: item to be matched
        :type: string
        :return: list of tweets
        """

        tweets = self.api.GetUserTimeline(screen_name='hardmob_promo', count=200)

        if item_match:

            tweets = [t for t in tweets if item_match in t.text.lower()]

        return [self._extract_data(t) for t in tweets]


def _extract_data_from_tweet(self, tweet):
    date = humanize_date(tweet.created_at)
    link = parse_link_from_text(tweet.text)
    text = tweet.text.replace(link, '').strip()

    return {
        'created_at': date,
        'text': text,
        'link': link,
    }

