import requests

# I found documentation here:
# https://www.mediawiki.org/wiki/API:Categorymembers

parameters = {'action' : 'query',
              'list' : 'categorymembers',
              'format' : 'json',
              'cmtitle' : 'Category:Programming languages created in 1991'}

wp_call = requests.get('http://en.wikipedia.org/w/api.php', params=parameters)

response = wp_call.json()

for page in response['query']['categorymembers']:
    print(page['title'])
