import twitter
import twitter_settings as ts
from datetime import date, timedelta
import re


def parse_link_from_text(text):
    if text:
        try:
            return re.search(r'https://(.*?)\S*', text).group(0)
        except Exception as e:
            pass
    return 'Not known'


class TwitterHandler(object):
    def __init__(self):
        self.api = twitter.Api(
                        consumer_key=ts.CONSUMER_KEY,
                        consumer_secret=ts.CONSUMER_SECRET,
                        access_token_key=ts.ACCESS_TOKEN_KEY,
                        access_token_secret=ts.ACCESS_TOKEN_SECRET
                    )

    def fetch_hardmob_promos(self, item_match=None, date_range=20):
        """
        Fetches hardmob sale's tweets and, if item_match given, returns only the ones with the item's text
        :param item_match: item to be matched
        :type: string
        :param date_range: Date range in days
        :type date_range: int
        :param log_error: error log function
        :return: list of tweets
        """

        tweets = self.api.GetUserTimeline(screen_name='hardmob_promo', count=200)
        if item_match:
            tweets = [t for t in tweets if item_match in t.text.lower()]
        return [{'item': t.text, 'created_at': t.created_at, 'link': parse_link_from_text(t.text)} for t in tweets]


if __name__ == '__main__':
    twitter = TwitterHandler()
    for tweet in twitter.fetch_hardmob_promos():
        print(tweet)
