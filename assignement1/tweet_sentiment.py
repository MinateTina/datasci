import sys
import json

def load_sentiments(f):
  afinnfile = open(f)
  scores = {} # initialize an empty dictionary
  for line in afinnfile:
    term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
    scores[term] = int(score)  # Convert the score to an integer.
  return scores;


def sentiment(t, sentiments):
  if t == None:
    return 0
  s = 0
  for word in t.split(" "):
    s += sentiments.get(word, 0)
  return s


def main():
    tweet_file = open(sys.argv[2])

    sentiments = load_sentiments(sys.argv[1])

    for tweet in open(sys.argv[2]).readlines():
        tweet = json.loads(tweet)
        text = tweet.get('text')
        print sentiment(text, sentiments)


if __name__ == '__main__':
    main()
