#!/Users/capo/anaconda/bin/python
# coding: utf-8
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import time
import json
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36'}

#latest
titles=[]
links=[]
pics=[]
dats=[]
for i in range(1,6):
    url ='http://www.cna.com.tw/search/hysearchws.aspx?q=%E4%B8%AD%E5%85%B119%E5%A4%A7%E5%B0%88%E9%A1%8C%EF%BC%88%20or%20%E4%B8%AD%E5%85%B119%E5%A4%A7%E7%8F%BE%E5%A0%B4%E5%81%B4%E8%A8%98&p={}'.format(i)
    res = requests.get(url,headers=headers)
    h2 = BeautifulSoup(res.text,'lxml').find_all('h2')
    for z in range(len(h2)):
        titles.append(h2[z].text)
    for x in range(len(h2)):
        img = BeautifulSoup(res.text,'lxml').find_all("div", { "class" : "list_pic" })[x].find('img')['data-src']
        if img!='':
            pics.append(img.replace('WebPhotos/200','WebPhotos/500'))
        else:
            pics.append('http://www.cna.com.tw/project/20170925-china/img/default.jpg')
    for y in range(len(h2)):
        link = BeautifulSoup(res.text,'lxml').find_all("div", { "class" : "search_result_list" })[0].find_all('a')[y]['href']
        links.append('http://www.cna.com.tw'+link)
#     for w in range(len(h2)):
#         date = BeautifulSoup(res.text,'lxml').find_all("div", { "class" : "search_result_list" })[0].find_all('a')[y]['href'].split('/')
#         t = d[1][:4]+'/'+d[1][4:6]+'/'+d[1][6:8]
#         dats.append(t)
for date in links:
    d = date.replace(r'http://www.cna.com.tw/news/','').split('/')
    t = d[1][:4]+'/'+d[1][4:6]+'/'+d[1][6:8]
    dats.append(t)

col=['link','img','title','date']
output = pd.DataFrame(columns = col)
output['link']=links
output['title']=titles
output['img']=pics
output['date']=dats

output.to_json('/Users/capo/Dropbox/articlelist.json',orient='records')

#expert
titles=[]
links=[]
pics=[]
dats=[]
for i in range(1,6):
    url ='http://www.cna.com.tw/search/hysearchws.aspx?q=%E4%B8%AD%E5%85%B119%E5%A4%A7%E5%B0%88%E5%AE%B6%E8%A7%A3%E6%9E%90&p={}'.format(i)
    res = requests.get(url,headers=headers)
    h2 = BeautifulSoup(res.text,'lxml').find_all('h2')
    for z in range(len(h2)):
        titles.append(h2[z].text)
    for x in range(len(h2)):
        img = BeautifulSoup(res.text,'lxml').find_all("div", { "class" : "list_pic" })[x].find('img')['data-src']
        if img!='':
            pics.append(img.replace('WebPhotos/200','WebPhotos/500'))
        else:
            pics.append('http://www.cna.com.tw/project/20170925-china/img/default.jpg')
    for y in range(len(h2)):
        link = BeautifulSoup(res.text,'lxml').find_all("div", { "class" : "search_result_list" })[0].find_all('a')[y]['href']
        links.append('http://www.cna.com.tw'+link)
#     for w in range(len(h2)):
#         date = BeautifulSoup(res.text,'lxml').find_all("div", { "class" : "search_result_list" })[0].find_all('a')[y]['href'].split('/')
#         t = d[1][:4]+'/'+d[1][4:6]+'/'+d[1][6:8]
#         dats.append(t)
for date in links:
    d = date.replace(r'http://www.cna.com.tw/news/','').split('/')
    t = d[1][:4]+'/'+d[1][4:6]+'/'+d[1][6:8]
    dats.append(t)

col=['link','img','title','date']
output = pd.DataFrame(columns = col)
output['link']=links
output['title']=titles
output['img']=pics
output['date']=dats

output.to_json('/Users/capo/Dropbox/expertlist.json',orient='records')

#behind
titles=[]
links=[]
pics=[]
dats=[]
for i in range(1,6):
    url ='http://www.cna.com.tw/search/hysearchws.aspx?q=%E4%B8%AD%E5%85%B119%E5%A4%A7%E7%8F%BE%E5%A0%B4%E5%81%B4%E8%A8%98&p={}'.format(i)
    res = requests.get(url,headers=headers)
    h2 = BeautifulSoup(res.text,'lxml').find_all('h2')
    for z in range(len(h2)):
        titles.append(h2[z].text)
    for x in range(len(h2)):
        img = BeautifulSoup(res.text,'lxml').find_all("div", { "class" : "list_pic" })[x].find('img')['data-src']
        if img!='':
            pics.append(img.replace('WebPhotos/200','WebPhotos/500'))
        else:
            pics.append('http://www.cna.com.tw/project/20170925-china/img/default.jpg')
    for y in range(len(h2)):
        link = BeautifulSoup(res.text,'lxml').find_all("div", { "class" : "search_result_list" })[0].find_all('a')[y]['href']
        links.append('http://www.cna.com.tw'+link)
#     for w in range(len(h2)):
#         date = BeautifulSoup(res.text,'lxml').find_all("div", { "class" : "search_result_list" })[0].find_all('a')[y]['href'].split('/')
#         t = d[1][:4]+'/'+d[1][4:6]+'/'+d[1][6:8]
#         dats.append(t)
for date in links:
    d = date.replace(r'http://www.cna.com.tw/news/','').split('/')
    t = d[1][:4]+'/'+d[1][4:6]+'/'+d[1][6:8]
    dats.append(t)

col=['link','img','title','date']
output = pd.DataFrame(columns = col)
output['link']=links
output['title']=titles
output['img']=pics
output['date']=dats

output.to_json('/Users/capo/Dropbox/behindlist.json',orient='records')

#album
stitle=[]
scaption=[]
simg=[]

url ='http://m.cna.com.tw/photoalbum/1067'
res = requests.get(url,headers=headers)
album = BeautifulSoup(res.text,'lxml').find_all('div',{"id":"galleria"})[0].find_all('img')

for i in album:
    stitle.append(i['data-title'])
    scaption.append(i['data-description'])
    simg.append(i['src'].replace('s.jpg','.jpg'))

col1=['title','caption','img']
phoalbum=pd.DataFrame(columns = col1)
phoalbum['title']=stitle
phoalbum['caption']=scaption
phoalbum['img']=simg
phoalbum.to_json('/Users/capo/Dropbox/album.json',orient='records')

print('done')