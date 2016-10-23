#!/usr/bin/python
#-*- coding: utf8 -*-

'''
function to search value on a list, receive two parameters list and value to search
'''

def search(lis, value):
    for x,e in enumerate(lis):
        if e == value:
            return x
    return None

L = []

while True:
    V = int(input("Value: "))
    if V == 0:
        break
    L.append(V)    
    
V_search = int(input("Search Value: "))
print(search(L, V_search))

'''
define the soma and average of a list
'''
def soma(L):
    total=0
    for e in L:
        total+=e
    return total

def media(L):
    return(soma(L)/len(L))    

print(soma(L))
print(media(L))

