# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 17:32:12 2019

@author: giles
"""

'''
Question 1
Can you remember how to check if a key exists in a dictionary?
Using the capitals dictionary below write some code to ask the user to input
a country, then check to see if that country is in the dictionary and if it is
print the capital. If not tell the user it's not there.
'''
def country_check():
    capitals={'France':'Paris', 'Spain':'Madrid', 'United Kingdom':'London', 'India': 'New Delhi', 'United States':'Washington DC', 'Italy': 'Rome', 'Denmark':'Copenhagen', 'Germany':'Berlin', 'Greece':'Athens', 'Bulgaria':'Sofia'}
    user_country = input("Please pick a Country:\n>>>")
    if user_country in capitals:
        print(capitals[user_country])
    else:
        print('The country you selected is not known.')


'''
Question 2
Write python code that will create a dictionary containing key, value pairs
that represent the first 12 values of the Fibonacci sequence
i.e {1:0,2:1,3:1,4:2,5:3,6:5,7:8 etc}
'''
def fib(seq):
    fibl = [0,1]
    x = 0
    y = 1
    while len(fibl) <= seq:
        nn = fibl[x] + fibl[y]
        fibl.append(nn)
        x +=1
        y +=1
    return fibl

def fib_dict():
    fibl = fib(12)
    fib_dict = {}
    for val in range(13):
        fib_dict[val]=fibl[val]
    print(fib_dict)

'''
Question 3
Create a dictionary to represent the open, high, low, close share price data
for 4 imaginary companies. 'Python DS', 'PythonSoft', 'Pythazon' and 'Pybook'
the 4 sets of data are [12.87, 13.23, 11.42, 13.10],[23.54,25.76,21.87,22.33],
[98.99,102.34,97.21,100.065],[203.63,207.54,202.43,205.24]
'''
fin_data = {'Python DS':[12.87, 13.23, 11.42, 13.10], 'PythonSoft':[23.54,25.76,21.87,22.33], 'Pythazon':[98.99,102.34,97.21,100.065], 'Pybook':[203.63,207.54,202.43,205.24]}


'''
Question 4
Go to the python module web page and find a module that you like. Play with it,
read the documentation and try to implement it.
'''
# I have lots of examples of this in my Data science projects

'''
Question 5
Create a dictoinary containing as keys the letters from A-Z, the values should
be random numbers created from the random module. Can you draw a bar graph of
the results?
'''
import random as r
import matplotlib.pyplot as plt

alpha_list = "abcdefghijklmnopqrstuvwxyz"
alpha_dict = {}
for let in alpha_list:
    for val in alpha_list:
        alpha_dict[val] = r.randint(1,100)
print(alpha_dict)

plt.bar(alpha_dict.keys(), alpha_dict.values())
plt.show()

'''
Question 6
Create a dictionary containing 4 suits of 13 cards
['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
'''

deck_of_cards = {'Hearts':['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King'], 'Diamonds':['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King'], 'Spades':['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King'], 'Clubs':['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']}

