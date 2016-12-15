from lxml import html
import requests
import urlparse
import sys
import os


siteurl = raw_input('Enter a web site url: ')
# siteurl = "deepmind.com/"
page = requests.get('http://' + siteurl)
foldername = siteurl.split(".")[1]
try:
    os.mkdir(foldername)
except:
    print foldername + " exists"

# Parse the body of the web page into a tree
parsed_body = html.fromstring(page.text)

# Grab links to iages using Xpath
# images will get a list of URLs of the images
images = parsed_body.xpath('//img/@src')
if not images:
    sys.exit("Found No Images")

# Convert any relative urls to absolute urls
images = [urlparse.urljoin(page.url, url) for url in images]
print '\n Found %s images' % len(images)

# Only download first 5 images
for url in images[0:5]:
    try:
        r = requests.get(url, stream=True)
        f = open(foldername+'/%s' % url.split('/')[-1], 'wb')
        f.write(r.content)
        f.close()
    except:
        print "not an image"
