#!/usr/bin/env python
# coding: utf-8

# In[2]:


import random
print("Welcome To Your Password Generator")
chars='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()><,./'
number=int(input("Amount of passwords to generate: "))
length=int(input("Input your password length: "))

print('\nHere are your passwords:')

for pwd in range(number):
    passwords=''
    for c in range(length):
        passwords+=random.choice(chars)
    print(passwords)

