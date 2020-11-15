#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: github.com/maliozer
@license: MIT
"""


import requests
from bs4 import BeautifulSoup

res = requests.request(url="https://www.hurriyet.com.tr/",method="GET")

#check the content
print(res.content[:200])

html_doc = res.content

soup = BeautifulSoup(html_doc, 'html.parser')

news_links = soup.findAll(name="a", attrs={"class":"news-link"})

all_links = soup.findAll(name="a")

image_elements = soup.findAll(name="img", attrs={"class": "news-image"})

#why we use set
alt_set = set()

for tag in image_elements:
    alt_set.add(tag.attrs['alt'])