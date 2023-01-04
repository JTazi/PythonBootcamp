# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 10:25:03 2023
Problem: 
    take string input of parentheses, square and curly brackets
    check if left and right brackets are equal and in the right order
    return True/False
"""
test1 = '({[]})'
test2 = '({[})]'


def bracket_balance(brackets):
    #create list to store left brackets in order
    left_stack = []
    #lists to identify lefts and rights
    lefts = ['(','{','[']
    rights = [')','}',']']
    #dictionary for storing bracket pairs
    brack_dict = {')':'(', ']':'[', '}':'{'}
    #iterate through input string and store left brackets in left_stack
    #once a right is encountered, check if it pairs with top of left_stack
    #if it matches, pop top of stack and continue
    for b in brackets:
        if b in lefts:
            left_stack.append(b)
        if b in rights:
            if left_stack[-1] == brack_dict[b]:
                left_stack.pop()
            else:
                return False
    #need to check stack is empty to ensure all lefts had pair
    #empty stack returns False, so inverse with not
    if not left_stack:
        return True
    else:
        return False
            

print(bracket_balance(test1))
print(bracket_balance(test2))
