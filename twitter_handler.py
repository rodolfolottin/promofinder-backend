import twitter
import twitter_settings as ts
import re
import arrow
from datetime import datetime


def parse_link_from_text(text):
    if text:
        try:
            return re.search(r'https://(.*?)\S*', text).group(0)
        except Exception as e:
            pass
    return 'Not known'


def humanize_date(string_date):
    if string_date:
        try:
            date = datetime_from_string(string_date)
            return arrow.get(date).humanize()
        except:
            pass
    return 'Not known'


def datetime_from_string(str_date):
    try:
        return datetime.strptime(re.sub(r'\+\d+\S', '', str_date), '%a %b %d %H:%M:%S %Y')
    except:
        return None


class TwitterHandler(object):
    def __init__(self):
        self.api = twitter.Api(
                        consumer_key=ts.CONSUMER_KEY,
                        consumer_secret=ts.CONSUMER_SECRET,
                        access_token_key=ts.ACCESS_TOKEN_KEY,
                        access_token_secret=ts.ACCESS_TOKEN_SECRET
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

    def _extract_data(self, tweet):
        date = humanize_date(tweet.created_at)
        link = parse_link_from_text(tweet.text)
        text = tweet.text.replace(link, '').strip()

        return {
                'created_at': date,
                'item': text,
                'link': link
            }

