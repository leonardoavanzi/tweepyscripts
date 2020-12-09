import tweepy
from tweepy import OAuthHandler, Stream, StreamListener
from keys import *

ciano = '\033[96m'
RESET = "\033[0;0m" # ""
# This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):
    
    
    def on_status(self, status):
        print('\x1b[1;31m'+'Tweet encontrado!')
        print('\033[92m'+'Enviado via:',status.source)
        print('\033[96m'+'Mensagem: ', status.text)
        print('\033[0;0m'+'ID do tweet: ', status.id)
        print('\x1b[1;37m'+'Tweet feito no dia:', status.created_at)
        print('-' * 20)
        return True
   
    def on_error(self, status):
        if (status == 420) or (status == 429):
            print("Erro na API")
            return False
         

if __name__ == '__main__':
     listener = StdOutListener()
     auth = OAuthHandler(consumer_key, consumer_secret)
     auth.set_access_token(access_token, access_token_secret)
     stream = Stream(auth, listener)
     tracker_subject = input('\x1b[1;33mInsira uma palavra/hastag: ')
     print('\x1b[1;31m'+'listener ativado!') # \x1b[1;37m = bold color
     stream.filter(track=[tracker_subject],is_async=True)

     
     
        
    

    
    
                                                    

   
