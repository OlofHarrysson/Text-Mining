from twython import Twython

APP_KEY = None
with open('twitterAppKey.txt', 'r') as f:
    APP_KEY = f.read()

ACCESS_TOKEN = None
with open('twitterToken.txt', 'r') as f:
    ACCESS_TOKEN = f.read()

twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)


lang = 'en'
count = 1
query = '#bible'


tweets = twitter.search(q=query, lang=lang, count=count)

print(tweets)
