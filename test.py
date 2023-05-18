from urllib import request
from urllib.request import Request, urlopen
import re

 
url = "https://www.stltoday.com/places/"
request_site = Request(url, headers={"User-Agent": "Mozilla/5.0"})
page = urlopen(request_site)
html = page.read().decode("utf-8")
pattern = '"list-group-item-heading"><a href=".*?"'
link = re.findall(pattern, html, re.IGNORECASE)
listoflinks = []
makenewurl = url.replace('/places/','')
for i in range (len(link)):
    if "/places/" in link[i]:
        listoflinks.append(makenewurl + (link[i].replace('"list-group-item-heading"><a href="','')))
        
for i in range (len(listoflinks)):
    listoflinks[i] = listoflinks[i].replace('amp;','')

#print(listoflinks[1])

url1 = "https://www.stltoday.com/places/?action=srch&limit=&sort=&zipcode=63101&radius=100&keyword="
request_site1 = Request(url1, headers={"User-Agent": "Mozilla/5.0"})
page1 = urlopen(request_site1)
html1 = page1.read().decode("utf-8")
pattern1 = 'search-results col-lg-9 col-md-8.*?"</'
link1 = re.split('<article class="business-search-default">',html1)
print(len(link1))
listoflinks1 = []


url2 = "https://www.stltoday.com/places/active_life/fishing/?action=srch&limit=&sort=&zipcode=63101&radius=100&keyword="
request_site2 = Request(url2, headers={"User-Agent": "Mozilla/5.0"})
page2 = urlopen(request_site2)
html2 = page2.read().decode("utf-8")
pattern2 = 'search-results col-lg-9 col-md-8.*?"</'
link2 = re.split("category sub-cat",html2)
print(len(link2))
listoflinks2 = []

emails = []

""" splitstring = re.split(">|<| |:",html)
for i in range (len(splitstring)):
    if "@" in splitstring[i] and (".com" in splitstring[i] or ".org" in splitstring[i] or ".edu" in splitstring[i]):
        emails.append(splitstring[i].replace('"',''))
emails = list(dict.fromkeys(emails))
print(emails) """