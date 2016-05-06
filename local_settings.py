'''
Local Settings for a heroku_ebooks account. #fill in the name of the account you're tweeting from here.
'''

#configuration
MY_CONSUMER_KEY = ' FUvt5oJ0nBLl7LsGo4Was8FAO'
MY_CONSUMER_SECRET = 'p0BU30GwntFxw4IksnwYDm1iA98uwHGU5qLmawZ3QrzA9OesXD'
MY_ACCESS_TOKEN_KEY = ' 319729108-IlmXRB6QVa7dvsn4DlXVpzbLKDZQc6TuK8XUuJdh'
MY_ACCESS_TOKEN_SECRET = 'WljgZmvQm5XuW8qSN6cldzU2BXGBQaa8Um0VLIXnfDof9'

SOURCE_ACCOUNTS = [''] #A list of comma-separated, quote-enclosed Twitter handles of account that you'll generate tweets based on. It should look like ["account1", "account2"]. If you want just one account, no comma needed.
ODDS = 8 #How often do you want this to run? 1/8 times?
ORDER = 2 #how closely do you want this to hew to sensical? 1 is low and 3 is high.
DEBUG = True #Set this to False to start Tweeting live
STATIC_TEST = False #Set this to True if you want to test Markov generation from a static file instead of the API.
TEST_SOURCE = ".txt" #The name of a text file of a string-ified list for testing. To avoid unnecessarily hitting Twitter API.
TWEET_ACCOUNT = "Twiterless_Dan" #The name of the account you're tweeting to.
