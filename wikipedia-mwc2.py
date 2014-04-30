import mwclient
site = mwclient.Site('en.wikipedia.org')

category = site.Pages['Category:University of Washington']
for page in category:
    print page.name
