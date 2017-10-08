import os
import tweepy
import textwrap
from time import sleep
from credentials import *
from sample import *

os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

thistext = textwrap.shorten(main(),140)
    
api.update_status(thistext)
print(thistext)