#!/usr/bin/env python
# coding: utf-8

# In[5]:


pip install pytube


# In[ ]:


from pytube import YouTube
url="https://www.youtube.com/watch?v=1MBR39rTEs8"  #Enter the url of the video you want to download
video=YouTube(url)
print(video.title) #prints the title of the youtube video
print(video.views)    #prints the views of the video

print(video.description)    #prints the description of the video
video=video.streams.get_highest_resolution()
video.download()  #downloads the video in your current directory

