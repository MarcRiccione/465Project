import requests
from bs4 import BeautifulSoup
import re
import time
from urllib.request import Request, urlopen
"""
source_code = requests.get('http://localhost:3000/')
soup = BeautifulSoup(source_code.content, 'lxml')
data = []
links = []

def remove_duplicates(l): # remove duplicates and unURL string
    for item in l:
        match = re.search("(?P<url>https?://[^\s]+)", item)
        if match is not None:
            links.append((match.group("url")))


for link in soup.find_all('a', href=True):
    data.append(str(link.get('href')))
flag = True
remove_duplicates(data)
while flag:
    try:
        print('here')
        for link in links:
            for j in soup.find_all('a', href=True):
                
                temp = []
                source_code = requests.get(link)
                soup = BeautifulSoup(source_code.content, 'lxml')
                temp.append(str(j.get('href')))
                remove_duplicates(temp)

                if len(links) > 10: # set limitation to number of URLs
                    break
            if len(links) > 10:
                break
        if len(links) > 10:
            break
    except Exception as e:
        print(e)
        if len(links) > 10:
            break
"""
def getUrl(url):
    #counter = 0
    #url = 'http://localhost:3000/HW4.exe'
    r = requests.get(url, allow_redirects=True)
    open('./downloads2/input.exe', 'wb').write(r.content)
    #counter += 1
"""
for url in links:
    print(url)
    #req = Request(url + half_url.encode('utf-8'), headers={'User-Agent': 'Mozilla/5.0'})
    #r = Request('http://localhost:3000/test.txt')
    #webpage = urllib.request.retrieve(url)
    #response = urlopen(r)

    url = 'http://localhost:3000/HW4.exe'
    r = requests.get(url, allow_redirects=True)
    open('./downloads2/textD' + str(counter) + '.txt', 'wb').write(r.content)
    counter += 1
"""

