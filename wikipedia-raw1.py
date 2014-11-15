import json
import requests

wp_call = requests.get('https://en.wikipedia.org/w/api.php?action=query&prop=revisions&titles=Main_Page&rvlimit=100&rvprop=timestamp|user&format=json')

response = json.loads(wp_call.content)

for page_id in response["query"]["pages"].keys():
    page_title = response["query"]["pages"][page_id]["title"]
    revisions = response["query"]["pages"][page_id]["revisions"]

    for rev in revisions:
        print page_title + "\t" + rev["user"] + "\t" + rev["timestamp"]

