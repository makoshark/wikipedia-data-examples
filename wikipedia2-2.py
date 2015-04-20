import requests

# base url:
# https://en.wikipedia.org/w/api.php?action=query&prop=revisions&titles=%s&rvlimit=100&rvprop=timestamp|user&format=json

pages = ["Benjamin Mako Hill", "University of Washington", "Data science"]

parameters = {'action' : 'query',
              'prop' : 'revisions',
              'rvlimit' : 100,
              'rvprop' : 'timestamp|user',
              'format' : 'json',
              'continue' : ''}
        
for page_title in pages:
    parameters['titles'] = page_title
    
    while True:
        wp_call = requests.get('https://en.wikipedia.org/w/api.php', params=parameters)
        response = wp_call.json()

        for page_id in response["query"]["pages"].keys():
            page_title = response["query"]["pages"][page_id]["title"]
            revisions = response["query"]["pages"][page_id]["revisions"]

            for rev in revisions:
                print(page_title + "\t" + rev["user"] + "\t" + rev["timestamp"])
                
        if 'continue' in response:
            parameters.update(response['continue'])
        else:
            break
