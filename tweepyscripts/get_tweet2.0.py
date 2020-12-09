import tweepy
import csv
import sys
from datetime import date

def tweets(username):
    
	auth = tweepy.OAuthHandler('XXXXXXXXXXXXXXXX', 'XXXXXXXXXXXXXXXX')
	auth.set_access_token('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX', 'XXXXXXXXXXXXXXXX')
	api = tweepy.API(auth)

	number_of_tweets = 400

	tweets_for_csv = []
	for tweet in tweepy.Cursor(api.user_timeline,api.search,q=username,screen_name = username, tweet_mode = 'extended').items(number_of_tweets):
		tweets_for_csv.append([username, tweet.created_at, tweet.full_text.encode("utf-8"),tweet.id_str])

	#write to a new csv file from the array of tweets
	outfile = username + "Files.csv"
	
	with open(outfile, 'w+') as file:
		writer = csv.writer(file, delimiter=',')
		writer.writerows(tweets_for_csv)

if __name__ == '__main__':
    #get tweets for username passed at command line
    if len(sys.argv) == 2:
        tweets(sys.argv[1])
    else:
        print("Error: enter one username")
