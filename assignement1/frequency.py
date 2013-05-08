import sys
import json


def main():

  wordfreq = dict()
  wordcount = 0

  for tweet in open(sys.argv[1]).readlines():
    tweet = json.loads(tweet)
    text = tweet.get('text')

    if text != None:
      words = text.split(" ")
      for word in words:
        wordcount += 1
        wordfreq[word] = wordfreq.get(word,0) + 1;

  for word in wordfreq:
    print word.encode('utf-8') + " " + str(wordfreq[word]*1.0/wordcount)



if __name__ == '__main__':
    main()
