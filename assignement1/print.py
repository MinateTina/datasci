import urllib
import json

q = "microsoft"

for p in range(1,11):
  response = urllib.urlopen("http://search.twitter.com/search.json?q=%s&page=%d" % (q, p))
  for k in json.load(response)['results']:
    tweet = k['text']
    tweet = tweet.replace("\n", "\\n")
    print tweet.encode('utf-8')
