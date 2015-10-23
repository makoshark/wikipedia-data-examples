import encoding_fix
import requests

# raw string:
# ?action=query&prop=revisions&titles=Python_(programming_language)&rvlimit=100&rvprop=timestamp|user&format=json')

# parameter version which makes a little more sense
parameters = {'action' : 'query',
              'prop' : 'revisions',
              'titles' : 'Python (programming language)',
              'rvlimit' : 100,
              'rvprop' : "timestamp|user",
              'format' : 'json',
              'continue' : ''}

while True:
    wp_call = requests.get('https://en.wikipedia.org/w/api.php', params=parameters)
    response = wp_call.json()
    print(parameters)
    print(response)

    for page_id in response["query"]["pages"].keys():
        page_title = response["query"]["pages"][page_id]["title"]
        revisions = response["query"]["pages"][page_id]["revisions"]

        for rev in revisions:
            print(page_title + "\t" + rev["user"] + "\t" + rev["timestamp"])

    if 'continue' in response:
        parameters.update(response['continue'])
    else:
        break
            
