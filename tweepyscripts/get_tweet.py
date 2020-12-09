import tweepy
from time import sleep # biblioteca pro delay
from datetime import date

print("Loading...")


CONSUMER_KEY = 'XXXXXXXXXXXXXXXX'
CONSUMER_SECRET = 'XXXXXXXXXXXXXXXX'
ACCESS_KEY = 'XXXXXXXXXXXXXXXX'
ACCESS_SECRET = 'XXXXXXXXXXXXXXXX'
today = date.today()

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
#print(api.me().name)

ciano = '\033[96m' # color in terminal output
RESET = "\033[0;0m" # ""

api.screen_name = input('\033[96m'+'type user @ here: ') #

for status in tweepy.Cursor(api.user_timeline, screen_name=api.screen_name, tweet_mode="extended",).items(100):
  #  print (status.created_at, tweet.id)
     print('\x1b[1;37m'+'Tweet feito no dia: ', status.created_at )
     print('\x1b[1;31m'+'\n Tweet: '+ '\x1b[1;34m' +status.full_text+'\n')
     sleep(1.2)


     
     
  
    

      

    
    

   
  
    
