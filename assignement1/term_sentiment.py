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

def sentimentalize(t, s, sentiments):
  if t != None:
    for word in t.split(" "):
      if (sentiments.get(word) == None):
        sentiments[word] = s/2
      else:
        sentiments[word] += s/2


def main():
    tweet_file = open(sys.argv[2])

    sentiments = load_sentiments(sys.argv[1])

    for tweet in open(sys.argv[2]).readlines():
        tweet = json.loads(tweet)
        text = tweet.get('text')
        s1 = sentiment(text, sentiments)
        sentimentalize(text, s1, sentiments)
        s2 = sentiment(text, sentiments)

    for k in sentiments:
      print k + " " + str(sentiments[k])


if __name__ == '__main__':
    main()
