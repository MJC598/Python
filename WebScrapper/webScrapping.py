import requests
from bs4 import BeautifulSoup
import pprint
import tldextract

#list of urls
aList = []
urlList = ['http://www.amazon.com/', 'http://missouri.edu/', 'http://www.google.com']


def connect(url, urlList):
    #creating my header to be identified by a website. basically telling them who is trying to scrap their site
    myHeader = {'user-agent': 'python-requests/4.8.2(Compatible; Mjc598; mailto:matthewjcarroll598@gmail.com)'}
    
    ext = tldextract.extract(url)
    
    #actually making the connection
    r = requests.get('http://{}.{}/robots.txt'.format(ext.domain, ext.suffix), headers=myHeader, timeout=15)
    
    #printing status_code
    if r.status_code != 200:
        if r.status_code == 404:
             print('Robots.txt not found')
        else:
             print(requests.status_code)
    
    return requests.get(url)

#getter to sort list
def getText(request):
    return request.text

#trying to find duplicates in a list

#LOGIC:
#   create array of aList.text
#   compare each element.text to the array
#   if not there add to array
#   if there do not add to array
#   return array
"""
def dupes(aList):
    clean = []
    seenText = []
    
    for x in aList:
        text = x.text
        for seen in seenText:
            if seen == text:
                break
            else
        if text not in seenText:
            seen[text] = 1
        else:
            if seen[text] == 1:
                d.append(x)
            seen[text] += 1
"""
    

def run():
    for url in urlList:
        site = connect(url, urlList)
        #creating an easy html parse variable
        info = BeautifulSoup(site.content, "html.parser")
        #looking for all links
        for a in info.find_all('a'):
            try:
                if a.get('href').startswith('http://') or a.get('href').startswith('http://'):
                    aList.append(a)
                    #print(a.text)
                    #print(a.get('href'))
            except AttributeError:
                print('Failed try/catch in run() function')
                pass
        aList.sort(key=lambda x: x.text, reverse=False)
        #dupes(aList)
        for item in aList:
            print(item.text)
            print(item.get('href'))
            
run()

