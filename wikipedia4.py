import requests

# ?action=query&titles=Albert%20Einstein&prop=categories
# Get the list of categories for the Albert Einstein article.

parameters = {'action' : 'query',
              'titles' : 'Albert Einstein',
              'prop' : 'categories',
              'format' : 'json',
              'continue' :  ''}

while True:
    wp_call = requests.get('http://en.wikipedia.org/w/api.php', params=parameters)
    response = wp_call.json()

    for page_id in response["query"]["pages"].keys():
        for category in response["query"]["pages"][page_id]['categories']:
            print(category['title'])

    if 'continue' in response:
        parameters.update(response['continue'])
    else:
        break

