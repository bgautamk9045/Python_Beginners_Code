#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
from pprint import pprint
API_KEY="cb771e45ac79a4e8e2205c0ce66ff633"
city= input("Enter a city: ")
print(city)
base_url="http://api.openweathermap.org/data/2.5/weather?appid="+API_KEY+"&q="+city
print(base_url)
weather_data=requests.get(base_url).json()
print(weather_data)


# In[ ]:




