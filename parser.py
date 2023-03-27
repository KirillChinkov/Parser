import requests
import numpy as np
import pandas as pd
import time
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import chardet
# first of all, i will emulate actions of a user
UserAgent().chrome
Out: 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2224.3 Safari/537.36'

page_link = 'https://www.______________.com/'

response = requests.get(page_link, headers={'User-Agent': UserAgent().chrome})
html = response.content
# then i copy and download a main page of the site
f = open('main page.html', 'w', encoding='utf-8')
f.write(response.text)
import re
# find all links on the page
urls = re.findall(r'href="([^"]*)"', open('main page.txt').read())
print(urls)



print(urls, sep='/n')
# add to a link the name of the site if it is not there
for i in range(len(urls)):
    # Check if the element starts with "https://www.classcentral.com"
    if not urls[i].startswith('https://www.classcentral.com'):
        # If not, add the text to the beginning of the element
        urls[i] = 'https://www.classcentral.com' + urls[i]

count=0
for i in urls:
    count+=1
    print(count)
    print(i)

# Print the modified list
print(urls)
# using the link list from urls and UserAgent i will create a file html with all code of a pages from the list
for i in range(len(urls)+1):
    response1 = requests.get(urls[i], headers={'User-Agent': UserAgent().chrome})
    # html = response.content
    # print(html)
    with open(f"{i}.html", 'w', encoding='utf-8') as f:
        if f.closed:
            f = open('file.html', 'w')
        f.write(response1.text)

