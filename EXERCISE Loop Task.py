#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 08:50:32 2019

@author: Giles
"""

'''
Question 1
Ask the user for two numbers between 1 and 100. Then count from the
lower number to the higher number. Print the results to the screen.
'''
def user_num():
    num1 = input('Pick a number between 1 and 100\n>>>')
    if num1.isdigit() is not True:
        print('That is not a number, goodbye.')
        return
    num1 = int(num1)
    if num1 < 1 or num1 > 100:
        print('That number is not between 1 and 100, goodbye')
        return
    
    num2 = input('Pick a second number between 1 and 100\n>>>')
    if num2.isdigit() is not True:
        print('That is not a number, goodbye.')
        return
    num2 = int(num2)
    if num2 < 1 or num2 > 100:
        print('That number is not between 1 and 100, goodbye')
        return
    
    mi = min(num1,num2)
    ma = max(num1,num2) + 1
    for val in range(mi,ma):
        print(val, end = ' ')

        

'''
Question 2
Ask the user to input a string and then print it out to the screen in
reverse order (use a for loop).
'''
def str_rev():
    name = input('Please type your name: \n>>>')
    for val in range(len(name)-1,-1,-1):
        print(name[val], end=' ')


'''
Question 3
Ask the user for a number between 1 and 12 and then display a times
table for that number.
'''
def times_table():
    num = int(input('Pick a number between 1 and 12: \n>>>'))
    mult_table = []
    lst = []
    for col in range(1,num+1):
        for row in range(1, num+1):
            lst.append(col*row)
        print(lst)
        mult_table.append(lst)
        lst = []
    # print(mult_table)
        

'''
Question 4
Can you amend the solution to question 3 so that it just prints out all
times tables between 1 and 12? (no  need to ask user for input)
'''
def tt12():
    num = 12
    mult_table = []
    lst = []
    for col in range(1,num+1):
        for row in range(1, num+1):
            lst.append(col*row)
        print(lst)
        mult_table.append(lst)
        lst = []

'''
Question 5
Ask the user to input a sequence of numbers. Then calculate the mean
and print the result
'''
def mean():
    lst = []
    cnt = 0
    num = input("Please pick a number, enter 'n' to end selection.\n>>>")
    if num == 'n':
        return
    while num != 'n':
        cnt += 1
        lst.append(int(num))
        num = input(f"Please pick a number, {cnt} numbers selected.\n>>>")
    tot = 0
    for val in lst:
        tot += val
    mn = tot / len(lst)
    print(f'Average is: {mn}')

'''
Question 6
Write code that will calculate 15 factorial. (factorial is product of
positive ints up to a given number. e.g 5 factorial is 5x4x3x2x1)
'''
def fact_15():
    prod = 1
    for val in range(1,16):
        prod = prod*val
    print(prod)

'''
Question 7
Write code to calculate Fibonacci numbers. Create list containing
first 20 Fibonacci numbers, (Fib  numbers made by sum of preceeding
two. Series starts 0 1 1 2 3 5 8 13 ....)
'''
def fib():
    fibl = [0,1]
    x = 0
    y = 1
    while len(fibl) < 20:
        nn = fibl[x] + fibl[y]
        fibl.append(nn)
        x +=1
        y +=1
    print(fibl)


'''
Question 8
The previous question was the first to contain comments. Go back
through the other questions in this file and add comments to the
solutions.
'''

'''
Question 9

     *****
     *
     ****
     *
     *
     *
Can you draw this using python? (comment the solution code)
'''
print('*****\n*\n***\n*\n*\n*')


'''
Question 10
Write some code that will determine all odd and even numbers
between 1 and 100. Put the odds in a list named odd and the evens
in a list named even.
'''
def odds_evens_sorter():
    odds = []
    evens = []
    for val in range(1,101):
        if val % 2 == 1:
            odds.append(val)
        else:
            evens.append(val)
    print(f'Evens: {evens}\nOdds: {odds}')
            







