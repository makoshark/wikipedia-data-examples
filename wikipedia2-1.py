import encoding_fix
import requests

url_base = 'https://en.wikipedia.org/w/api.php?action=query&prop=revisions&titles=%s&rvlimit=100&rvprop=timestamp|user&continue=&format=json'

pages = ["Benjamin Mako Hill", "Python", "Data science"]

for page_title in pages:
    
    wp_call = requests.get(url_base % page_title)
    response = wp_call.json()

    for page_id in response["query"]["pages"].keys():
        page_title = response["query"]["pages"][page_id]["title"]
        revisions = response["query"]["pages"][page_id]["revisions"]

        for rev in revisions:
            print(page_title + "\t" + rev["user"] + "\t" + rev["timestamp"])

