""" Streaming twitter API example """

# authors: Phil Mui, Michele Samorani, Yuhao Wang

#Updated by Emma
import sys
from tweepy import StreamingClient, StreamRule 
class TwitterListener(StreamingClient):
    """ Twitter stream listener. """
    def on_tweet(self, tweet):
        f.write(str(tweet.text.encode('utf-8') + b"\n"))
        f.flush()
        print(tweet.text.encode('utf-8'))
        sys.stdout.flush()
	
    def on_errors(self, status_code):
        if status_code == 420:
            #returning False in on_error disconnects the stream
            return False

if __name__ == "__main__":
    try:
        if len(sys.argv) != 2:
            print("Usage: %s <word>" % (sys.argv[0]))
        else:
            word = sys.argv[1]
            f = open(word + '.txt', 'w')
            stream = TwitterListener('AAAAAAAAAAAAAAAAAAAAAC39hgEAAAAAPxFK%2FOMWGOr0TXJoGBq7JOEXAqg%3DxiULNh0sKb7scJIuq7XtMfwnBz1hnSHgNM55svqr92wnP6mNZG') #Add your bearer token as string

            print("Listening to " + word + " and #" + word)
            print("Tweets are written to your_key_word.txt")
            print("Press CTRL + c to terminate...")
            currentRules = stream.get_rules().data
            if currentRules is not None: 
                stream.delete_rules(currentRules)
            stream.add_rules([StreamRule(f"{word} lang:en"), StreamRule(f"#{word} lang:en")])
            stream.filter()
            

    except KeyboardInterrupt:
        f.close()
        print('*****************************\nInterrupted')
        sys.exit()
