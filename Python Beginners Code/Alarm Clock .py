#!/usr/bin/env python
# coding: utf-8

# In[4]:


pip install playsound


# In[12]:


#Alarm clock will play music at the alarmed time
import datetime
from playsound import playsound
alarmHour=int(input("Enter Hour: "))
alarmMin=int(input("Enter Minutes: "))
alarmAm=input("am / pm: ")

if alarmAm=="pm":
    alarmHour+=12

while True:
    if alarmHour==datetime.datetime.now().hour and alarmMin==datetime.datetime.now().minute:
        print("Playing...")
        os.startfile(r"C://Users//b0268660//Desktop//personal//Recordings//Voice Recorder//Dil ko karar.m4a") #Enter the path of a song or ringtone where it is placed in your system
        break;

