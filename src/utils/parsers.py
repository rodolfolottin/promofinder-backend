import re

import arrow


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

