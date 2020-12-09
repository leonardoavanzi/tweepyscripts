import tweepy
import time

# API tokens here
auth = tweepy.OAuthHandler('XXXXXXXXXXXXXXXXXXXXXXXXXX', 'XXXXXXXXXXXXXXXXXXXX')
auth.set_access_token('XXXXXXXXXXXXXXXXXXXXXXXXXXX', 'XXXXXXXXXXXXXXXXXXXXXXXXXXXX')

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

FILE_NAME = 'storage/last_seen_id.txt'

 
backpack = ["😯😯", "OPERAÇÃO NAKAS"] 

def retrieve_last_seen_id(file_name):
	f_read = open(file_name, 'r')
	last_seen_id = int(f_read.read().strip())
	f_read.close()
	return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
	f_write = open(file_name, 'w')
	f_write.write(str(last_seen_id))
	f_write.close()
	return

def reply_to_tweets():
	last_seen_id = retrieve_last_seen_id(FILE_NAME)	
	mentions= api.mentions_timeline(last_seen_id,tweet_mode='extended')

#storage the mention id and reply 
	for mention in reversed(mentions):
		print(str(mention.id)+'\n Mention: '+mention.full_text)
		last_seen_id = mention.id
		store_last_seen_id(last_seen_id, FILE_NAME)
		if 'operação nakas ' or 'api teste' in mention.full_text.lower():
			print('\x1b[1;31m'+'Encontrado!')
			print('\x1b[1;37m'+'Respondendo de volta...')
			api.update_status(backpack[0], mention.id)
			
while True:
	reply_to_tweets()
	time.sleep(15)
