# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 13:31:54 2022

@author: tazma
"""

# Two Sum problem
'''
Iterate through list of integers and return the indexes of the two numbers
that add up to target value.
'''

def two_sum(lst, tgt):
    for val in lst:
        indx = []
        if tgt-val in lst and tgt-val != val:
            indx.append(lst.index(val))
            indx.append(lst.index(tgt-val))
            return indx
        else:
            indx = -1
    return indx





lst1 = [2,5,3,7,4]        



