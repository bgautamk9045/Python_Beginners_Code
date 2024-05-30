#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random

def hangman():
    list_words = ['c', 'java', 'python', 'sql', 'reactjs', 'nodejs', 'sql', 'plsql']
    word = random.choice(list_words)
    turns = 10
    guessmade = ''
    entries = set('abcdefghijklmnopqrstuvwxyz')

    while len(word) > 0:
        main_word = ""

        for letter in word:
            if letter in guessmade:
                main_word += letter
            else:
                main_word += "_ "

        if main_word == word:
            print(main_word)
            print("You won!!")
            break;

        print("Guess the word:", main_word)
        guess = input()

        if guess in entries:
            guessmade += guess
        else:
            print("Enter a valid character")
            guess = input()

        if guess not in word:
            turns -= 1

            if turns == 9:
                print("9 turns left!!")
                print("--------------")
            if turns==8:
                print("8 turns left!!")
                print("--------------")
                print("      o       ")
                print("--------------")
            if turns==7:
                print("7 turns left!!")
                print("--------------")
                print("      o       ")
                print("      |       ")
                print("--------------")
            if turns==6:
                print("6 turns left!!")
                print("--------------")
                print("      o       ")
                print("      |       ")
                print("     /       ")
                print("--------------")
            if turns==5:
                print("5 turns left!!")
                print("--------------")
                print("      o       ")
                print("      |       ")
                print("     / \      ")
                print("--------------")
            if turns==4:
                print("4 turns left!!")
                print("--------------")
                print("     \o       ")
                print("      |       ")
                print("     / \      ")
                print("--------------")
            if turns==3:
                print("3 turns left!!")
                print("--------------")
                print("     \o/      ")
                print("      |       ")
                print("     / \      ")
                print("--------------")
            if turns==2:
                print("2 turns left!!")
                print("--------------")
                print("     \o/ |    ")
                print("      |       ")
                print("     / \      ")
                print("--------------")
            if turns==1:
                print("1 turns left!!")
                print("--------------")
                print("     \o/_|    ")
                print("      |       ")
                print("     / \      ")
                print("--------------")

            if turns == 0:
                print("0 turns left!!")
                print("--------------")
                print("     \o/_|    ")
                print("      |       ")
                print("     / \      ")
                print("----     -----")
                print("You lose!!")
                break

name = input("Enter name: ")
print("Welcome", name, "!")
print("Guess the word in less than 10 attempts!")
hangman()

