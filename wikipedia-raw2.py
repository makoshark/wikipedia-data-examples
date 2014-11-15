import time
import json
import requests

url_base = 'https://en.wikipedia.org/w/api.php?action=query&prop=revisions&titles=%s&rvlimit=100&rvprop=timestamp|user&format=json'

pages = ["Benjamin_Mako_Hill", "Python", "Data_science"]

for page_title in pages:
    
    wp_call = requests.get(url_base % page_title)
    response = json.loads(wp_call.content)

    for page_id in response["query"]["pages"].keys():
        page_title = response["query"]["pages"][page_id]["title"]
        revisions = response["query"]["pages"][page_id]["revisions"]

        for rev in revisions:
            print page_title + "\t" + rev["user"] + "\t" + rev["timestamp"]


    time.sleep(3)
