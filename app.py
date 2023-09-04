import logging
from pathlib import Path

import os
from instagrapi import Client
from instagrapi.exceptions import LoginRequired
from instagrapi.utils import random_delay
import feedparser

QUOTES_API_URL = 'https://api.api-ninjas.com/v1/quotes'

logger = logging.getLogger()
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.INFO)

cl = Client(delay_range=[1, 3])

QUOTES_API_KEY = os.environ.get('QUOTES_API_KEY')
if not QUOTES_API_KEY:
    logger.error("QUOTES_API_KEY environment variable is not set")
    exit(1)

try:

    session = cl.load_settings(Path("session.json"))
    cl.set_settings(session)

except LoginRequired:

    logger.error("Session is invalid")
    exit(1)

except Exception as e:

    logger.error("Couldn't login user using session information: %s" % e)
    exit(1)


def brainyquote():
    url = f"https://www.brainyquote.com/link/quotebr.rss"
    feed = feedparser.parse(url)
    summary = feed.entries[0]['summary']
    # Remove \" if at beginning and end of string, but not if in middle
    if summary.startswith('\"') and summary.endswith('\"'):
        summary = summary[1:-1]
    title = feed.entries[0]['title']
    return f"{summary} - {title}"


while True:

    try:

        # response = requests.get(QUOTES_API_URL, headers={'X-Api-Key': QUOTES_API_KEY}).json()[0]

        # quote = response['quote'] + " - " + response['author']

        quote = brainyquote()

        logger.info(quote)

        try:

            # audience: 0: followers, 1: best friends
            cl.create_note(quote, audience=0)
            random_delay([3600 * 18, 3600 * 28])

        except Exception as e:

            print("Couldn't create note: %s" % e)
            random_delay([3600 * 6, 3600 * 12])
            pass

    except Exception as e:

        print("Couldn't get quote: %s" % e)
        random_delay([3600 * 1, 3600 * 2])
