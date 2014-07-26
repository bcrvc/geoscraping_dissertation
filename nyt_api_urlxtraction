'''
script for getting the article data out of NYT API ...
extract the articles URLs and store them into a .txt file
'''

import urllib
import json

# get the dataset via NYT API 
# guide to constructing a search query: http://developer.nytimes.com/docs/read/article_search_api_v2#h2-queries
htmltext = urllib.urlopen('http://api.nytimes.com/svc/search/v2/articlesearch.json?q=%22e+waste%22&page=0&sort=oldest&api-key=495aa6a0e1c0ccb0bff6d7373cc918f9:6:69596355')
data = json.load(htmltext)

# open a .txt file 
myfile = open('urls.txt', 'w') 

# extract all URLs and store them into a .txt file 
for doc in data['response']['docs']:
	  # if print/write doc = whole data file 
    url = doc['web_url']
    print url
    myfile.write('%s\n' % url)

myfile.close()
