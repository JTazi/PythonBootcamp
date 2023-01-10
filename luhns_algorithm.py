# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 10:43:30 2023
Luhns Algorithm
1. multiply every 2nd digit by starting with 2nd from last, add those digits together
2. add value from step 1 to sum of digits not multiplied by 2
3. divide value from step 2 by 10, remainder 0 == valid
@author: John Tazioli
"""

def luhn_algo(cc):
    even = []
    odd = []
    output = None
    #convert cc number to string to use split function
    cc_str = str(cc)
    #split input into even and odd index list
    for x in range(0,len(cc_str)):
        if x % 2 == 0:
            even.append(cc_str[x])
        else:
            odd.append(cc_str[x])
    #convert string digits back to ints
    odd = list(map(lambda x: int(x),odd))
    even = list(map(lambda x: int(x),even)) 
    #step1
    odd = list(map(lambda x: 2*x, odd))
    odd_sum = 0
    for x in odd:
        odd_sum += x % 10
        odd_sum += x // 10
    #step2
    even_sum = sum(even)
    #step3
    tot_sum = odd_sum + even_sum
    if tot_sum % 10 == 0:
        output = True
    else:
        output = False
    print(f'Odd list = {odd} \n even list = {even}')
    print(f'Odd sum = {odd_sum} \n even sum = {even_sum}')
    return output
        
    