#!/usr/bin/env python
#-*- coding: utf8 -*-
'''
Created on 23 de ago de 2016

@author: Mauro Cesar de Oliveira
'''

'''
This program find the highest value, 
lower value and the average value on a list.
'''

L = []
#input the value on a list
while True:
    n = int(input("Type Number | 0 to exit: "))#the input exit can be changed, if you need to use the zero"0"
    if n == 0:
        break #exit of list
    L.append(n)

print(L)
#declares the values of the first position
maxi = L[0]
mini = L[0]
x = 0

#iterate the list maximum values and the minimum values
for e in L:
    if e > maxi:
        maxi = e
    if e < mini:
        mini = e 
    x = e + x
    average = (x / len(L)) #len(L) is how many values the list have     
print("Max Value: ", maxi) 
print("Min Value: ", mini)
print("Average Value: ", average)

