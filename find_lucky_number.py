# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 22:29:55 2018

@author: lijie
"""
#if there is an '8' in the number, it is a lucky number

#recursion method
def checkLucky1(num):
    if num==0:
        return False
    quotient,lastDigit=divmod(num,10)
    if lastDigit==8:
        return True
    return checkLucky1(quotient)

def checkLucky2(num):
    return '8'in str(num)

#test
if __name__=='__main__' :
    print('give a number:')
    a=int(input())
    if checkLucky1(a):
        print(a)
    if checkLucky2(a):
        print(a)
    
    

    