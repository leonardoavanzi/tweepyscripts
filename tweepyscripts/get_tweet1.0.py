import tweepy
import csv
#import pandas as pd
from datetime import date
from time import sleep
import sys


####input your credentials here
consumer_key = 'XXXXXXXXXXXXXXXX'
consumer_secret = 'XXXXXXXXXXXXXXXX'
access_token = 'XXXXXXXXXXXXXXXX'
access_token_secret = 'XXXXXXXXXXXXXXXX'
today = date.today()

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
api = tweepy.API(auth)

def on_error(self, status):
    print(status)
    if (status == 420):
        print("Error")
    return false
    
csvFile = open('konoha_backpack.csv', 'w' ) 
csvWriter = csv.writer(csvFile)

number_of_tweets = 300

for tweet in tweepy.Cursor(api.search,q="ribamar",count=1,since=today,tweet_mode = 'extended').items(number_of_tweets):
                          
    print (tweet.user.name.encode('utf-8'),tweet.id, tweet.created_at)
    csvWriter.writerow([tweet.created_at, tweet.full_text.encode('utf-8'), tweet.id, tweet.user.name.encode('utf-8'), tweet.user.screen_name.encode('utf-8')])
    