from urllib import request
from urllib.request import Request, urlopen
import re


def listL(url, n, k):
    if k is None:
        k = []
    request_site = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    page = urlopen(request_site)
    html = page.read().decode("utf-8")
    link = re.split('refine-search col-lg-3 col-md-4 visible-lg-block visible-md-block hidden-print',html)
    link = re.split('search-results col-lg-9 col-md-8',link[1])
    link = re.split('"category sub-cat"',link[0])
    if len(link) == 1:
        print(n)
    else:
        isolateList = []
        listoflinks = []
        for i in range (len(link)):
            link[i] = re.split('"',link[i])
            for j in range (len(link[i])):
                if "/places/" in link[i][j]:
                    isolateList.append(link[i][j])
        for i in range (n, len(isolateList) - 1):
            if "/places/" in isolateList[i]:
                listoflinks.append("https://www.stltoday.com" + isolateList[i])
                
        for i in range (len(listoflinks)):
            listoflinks[i] = listoflinks[i].replace('amp;','')
            if listoflinks[i] is not None:
                k.append(url)
                listL(listoflinks[i],n+1,k)
    return k
    
        
       
        
    
        
print(len(listL("https://www.stltoday.com/places/?action=srch&limit=&sort=&zipcode=63101&radius=100&keyword=", 0, [])))


