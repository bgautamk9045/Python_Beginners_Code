#!/usr/bin/env python
# coding: utf-8

# In[10]:


#program to get the github user image through username
import requests
from bs4 import BeautifulSoup as bs

github_user=input("Input Github Username: ")
url='https://github.com/'+github_user
r=requests.get(url)
soup=bs(r.content,'html.parser')
profile_image=soup.find('img')['src']
print(profile_image)

