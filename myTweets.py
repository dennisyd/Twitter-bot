import nltk
nltk.data.path.append('./nltk_data/')
import local_settings
import tweepy
import imdb
import sys
import random
import requests
import os
from RndSentence import RndSentence
from time import time as time

class TwitterAPI:

    def __init__(self):
        print 'initalizing movie cat, twitter bot'
        t0 = time()

        consumer_key = local_settings.MY_CONSUMER_KEY
        consumer_secret = local_settings.MY_CONSUMER_SECRET
        access_key = local_settings.MY_ACCESS_TOKEN_KEY
        access_token = local_settings.MY_ACCESS_TOKEN_SECRET

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_key, access_token)

        self.api = tweepy.API(auth)
        self.movies = imdb.IMDb()
        #this could cause a timeout adds 13 seconds....
        self.criticReview = RndSentence()

        t1 = time()
        loadTime = str((t1-t0))
        print 'movie cat initalized: ' + loadTime

    def rating_analysis(self, movie):
        rating = movie.get('rating')

        #print 'rating: ' + str(rating)
        #print 'rating type: ' + str(type(rating))

        if type(rating) is float:
            #print 'has a rating'
            movie_review_analysis = str(rating) + '/10 stars.'
        else:
            #print 'no rating'
            movie_review_analysis = ''


        return movie_review_analysis

    def tweet(self, message):
        tweet = message
        self.api.update_status(tweet)

    def tweet_with_media(self,url,message):
        filename = 'temp.jpg'
        tweet = message
        request = requests.get(url, stream=True)
        if request.status_code == 200:
            with open(filename, 'wb') as image:
                for chunk in request:
                    image.write(chunk)

            print 'tweeting with media'
            self.api.update_with_media(filename,tweet)
            os.remove(filename)
        else:
            print 'found media but could not download'
            self.api.update_status(tweet)

    def tweetMovie(self):
        flag = 1
        picture_flag = 1
        coverUrl = ''
        tweet = 'debugging'
        while flag == 1:
            flag = 0
            movie_id = random.randint(0, 1000000)

            movie = self.movies.get_movie(movie_id)
            kind = movie['kind']
            rating = self.rating_analysis(movie)
            title = movie.get('long imdb title')

            title = title.encode('ascii', 'ignore').decode('ascii')

            print 'full title: ' + str(title)
            print 'kind: ' + str(movie['kind'])
            print 'stars: ' + str(rating)

            movie_info = "%s. %s" % (title, rating)
            print movie_info


            review = self.criticReview.rndCriticReview()
            tweet = str(movie_info) + str(review)

            if(len(tweet) > 140):
                flag = 1

            if(kind != 'movie'):
                flag = 1

        try:
            coverUrl = movie['cover url']
        except:
            picture_flag = 0

        if picture_flag == 1:
            print 'tweeting with media'
            self.tweet_with_media(coverUrl,tweet)
        else:
            print 'tweeting without media'
            self.api.update_status(tweet)

        print 'TWEETED: ' + tweet

if __name__ == '__main__':
    t0 = time()
    twitter = TwitterAPI()
    #twitter.tweet("Dom is cool")
    twitter.tweetMovie()
    t1 = time()
    print 'runtime: ' + str(t1-t0)
