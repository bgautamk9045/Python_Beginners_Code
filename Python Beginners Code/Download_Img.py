#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
url=input("Enter the image url: ")
post=requests.get(url)

#file handling...
open('bharti.jpg','wb').write(post.content)
print("FILE DOWNLOADED SUCCESSFULLY...")

