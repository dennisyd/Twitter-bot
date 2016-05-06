import local_settings
import tweepy
import sys


class TwitterAPI:

    def __init__(self):
        consumer_key = local_settings.MY_CONSUMER_KEY
        consumer_secret = local_settings.MY_CONSUMER_SECRET
        access_key = local_settings.MY_ACCESS_TOKEN_KEY
        access_token = local_settings.MY_ACCESS_TOKEN_SECRET

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_key, access_token)

        self.api = tweepy.API(auth)

    def tweet(self, message):
        self.api.update_status(message)


if __name__ == '__main__':
    twitter = TwitterAPI()
    twitter.tweet("Dom is cool")