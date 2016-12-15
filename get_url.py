from lxml import html
import requests
import urlparse
import sys
import os


siteurl = raw_input('Enter a web site url: ')
# get the web page using the requests.get module
page = requests.get('http://' + siteurl)

# Parse the body of the web page into a tree
parsed_body = html.fromstring(page.text)

# Grab links to iages using Xpath
links = parsed_body.xpath('//a/@href')
if not links:
    sys.exit("Found No Links")

# Convert any relative urls to absolute urls
absolute_url = [urlparse.urljoin(page.url, url) for url in links]

# these next two lines filter out duplicates using the set command and element
# set holds unique values in Python
set = set(absolute_url)
# back to a list format
absolute_url = list(set)
print '\n Found %s links\n\n' % len(absolute_url)
# print all links
for i in absolute_url:
    print i
