import local_settings
import tweepy
import imdb
import sys
import random
import requests
import os


class TwitterAPI:

    def __init__(self):
        consumer_key = local_settings.MY_CONSUMER_KEY
        consumer_secret = local_settings.MY_CONSUMER_SECRET
        access_key = local_settings.MY_ACCESS_TOKEN_KEY
        access_token = local_settings.MY_ACCESS_TOKEN_SECRET

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_key, access_token)

        self.api = tweepy.API(auth)
        self.movies = imdb.IMDb()

    def rating_analysis(self, movie_id):

        try:
            rating = self.movies.get_movie_critic_reviews(movie_id)
        except:
            rating = -1

        if rating == -1:
            movie_review_analysis = 'nvr reviewed'
        elif rating <= 1:
            movie_review_analysis = 'BAD'
        elif rating <= 2:
            movie_review_analysis = 'Eh!'
        elif rating <= 3:
            movie_review_analysis = 'Okay'
        elif rating <= 4:
            movie_review_analysis = 'Good'
        else:
            movie_review_analysis = 'Great!'

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
        while flag == 1:
            flag = 0

            movie_id = random.randint(0, 100000)
            movie = self.movies.get_movie(movie_id)

            review = self.rating_analysis(movie_id)

            tweet = '%s was produced in %s. It was %s' % (movie['title'], movie['year'], review)

            try:
                coverUrl = movie['cover url']
            except:
                picture_flag = 0

            if len(tweet) > 140:
                tweet = '%s was produced in %s' % (movie['title'], movie['year'])

            if len(tweet) > 140:
                tweet = '%s has a long title' % (movie['title'])

            if len(tweet) > 140:
                flag = 1

        if picture_flag == 1:
            self.tweet_with_media(coverUrl,tweet)
        else:
            print 'tweeting without media'
            self.api.update_status(tweet)

if __name__ == '__main__':
    twitter = TwitterAPI()
    #twitter.tweet("Dom is cool")
    twitter.tweetMovie()