#!/usr/bin/env python
# coding: utf-8

# In[1]:


#taking email id from the user
emailId=input("Enter your email address: ").strip()

#getting username from the email id
userName=emailId[:emailId.index("@")]

#getting domain name from the email id
domainName=emailId[emailId.index("@")+1:]

#storing username and domain name in final output variable
final_string=f"Your username is {userName} and your domain name is {domainName}"

#printing final output
print(final_string)

