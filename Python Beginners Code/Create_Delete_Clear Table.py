#!/usr/bin/env python
# coding: utf-8

# In[2]:


from prettytable import PrettyTable
table=PrettyTable(["S.no","Company_name","E.name","Experience"])

#adding rows in table
table.add_row(["0","Airtel","Parvesh","1.5 years"])
table.add_row(["1","Airtel","Bharti","1.5 years"])
table.add_row(["2","Airtel","Tinku","1.3 years"])
table.add_row(["3","Microsoft","Vishal","1.8 years"])
print(table)

#deleting the row from the table
table.del_row(0)
print(table)

#clear all the rows
table.clear_rows()
print(table)



