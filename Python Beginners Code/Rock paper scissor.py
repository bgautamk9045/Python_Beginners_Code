#!/usr/bin/env python
# coding: utf-8

# In[9]:


import random
def play():
    user=input("What's your choice? 'r' for Rock,'p' for paper,'s' for scissor : ")
    computer=random.choice(['r','p','s'])
    print("Computer's choice : ",computer)
    if(user==computer):
        return "It's a tie"
    
    # cases r>s,s>p,p>r
    if is_win(user,computer):
        return 'You won!'
    return 'You lost!'

def is_win(player,opponent):
    #return true if player wins
    #r>s,s>p,p>r
    if(player=='r' and opponent == 's') or (player == 's' and opponent=='p') or (player=='p' and opponent=='r'):
        return True

    
print(play())   


# In[ ]:





# In[ ]:




