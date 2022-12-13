# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 15:17:56 2019

@author: giles
"""

'''
Question 1

Create a class to represent a bank account. It will need to have a balance,
a method of withdrawing money, depositing money and displaying the balance to
the screen. Create an instance of the bank account and check that the methods
work as expected.
'''
class bank_account_v1(object):

    def __init__(self, init_balance):
        self.balance = init_balance
        print(f'Account Balance: {self.balance}')
    
    def withdraw(self, w_amount):
        self.balance -= w_amount
        # print(f'New Account Balance: {self.balance}')
        
    def deposit(self, d_amount):
        self.balance += d_amount
        # print(f'New Account Balance: {self.balance}')
        
    def check(self):
        print(f'Account Balance: {self.balance}')
        
        
class bank_account_v2(object):
    '''
    A class used to represent a bank account balance.
    Attributes:
        init_balance : float
            used to track initial account balance
        balance : float
            account balance
        w_amount : float
            withdraw amaount
        d_amount : float
            deposit amount
    
    Methods:
        withdraw()
            ask user for withdraw amount and subtract from balance
        deposit()
            ask user for deposit amount and add to balance
        check()
            tell user account balance
    '''
    def __init__(self, init_balance=0.0):
        self.balance = init_balance
        print(f'Account Balance: {self.balance}')
    
    def withdraw(self):
        w_amount = float(input('How much money would you like to withdraw? \n>>>'))
        if self.balance >= w_amount:
            self.balance -= w_amount
        else:
            print(f'Account Balance: {self.balance}\nNot enough funds.')
        # print(f'New Account Balance: {self.balance}')
        
    def deposit(self):
        d_amount = float(input('How much money would you like to deposit? \n>>>'))
        self.balance += d_amount
        # print(f'New Account Balance: {self.balance}')
        
    def check(self):
        print(f'Account Balance: {self.balance}')
    


'''
Question 2
 Create a circle class that will take the value of a radius and
 return the area of the circle
'''

class circle(object):
    def __init__(self, radius=0):
        if radius == 0:
            self.radius = int(input('Please enter the radius of the circle: \n>>>'))
        else:
            self.radius = radius
                
    def area(self):
        pi = 3.14
        self.area = pi*self.radius*self.radius
        print(f'Area of the circle is {self.area}')
