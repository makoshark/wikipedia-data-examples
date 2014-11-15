import time
import json
import mwclient

def format_time(t):
    return(time.strftime('%Y-%m-%d %H:%M:%S', t))

site = mwclient.Site('en.wikipedia.org')

page = site.Pages["Data science"]

for revision in page.revisions():
    print revision["user"] + "\t" + format_time(revision['timestamp'])
