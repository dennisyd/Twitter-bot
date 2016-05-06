import local_settings
import tweepy
import imdb
import sys
import random


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
        tweet = message
        self.api.update_status(tweet)

    def tweetMovie(self):
        movies = imdb.IMDb()
        movie_id = random.randint(0, 100000)
        movie = movies.get_movie(movie_id)
        print movie.keys()
        tweet = '%s was produced in %s' % (movie['title'], movie['year'], )

        self.api.update_status(tweet)


if __name__ == '__main__':
    twitter = TwitterAPI()
    #twitter.tweet("Dom is cool")
    twitter.tweetMovie()