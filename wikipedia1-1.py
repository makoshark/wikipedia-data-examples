import requests

wp_call = requests.get('https://en.wikipedia.org/w/api.php?action=query&prop=revisions&titles=Python_(programming_language)&rvlimit=100&rvprop=timestamp|user&continue=&format=json')

response = wp_call.json()

for page_id in response["query"]["pages"].keys():
    page_title = response["query"]["pages"][page_id]["title"]
    revisions = response["query"]["pages"][page_id]["revisions"]

    for rev in revisions:
        print(page_title + "\t" + rev["user"] + "\t" + rev["timestamp"])

