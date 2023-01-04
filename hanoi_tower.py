# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 11:01:03 2023
Problem: Towers of Hanoi
Create function to calculate the number of moves required to solve
tower problem with n disks
- 3 towers
- can't move big piece on top of small piece'
"""

#3 towers A,B,C
A = [3,2,1]
B = []
C = []

count = 0

def towers_of_hanoi(A,B,C,n):
    global count
    
    #base case when 1 disk
    if n == 1:
        #pop disk off of tower A, onto tower B
        disk = A.pop()
        C.append(disk)
        count +=1
    else:
        #these three moves are for 2 disks, the base case when dealing with 3 poles
        #scales up with n disks
        # move disk from A to B, the bottom disk
        towers_of_hanoi(A, C, B, n-1)
        # move disk from A to C
        towers_of_hanoi(A, B, C, 1)
        #move disk from B to C
        towers_of_hanoi(B, A, C, n-1)
        return count