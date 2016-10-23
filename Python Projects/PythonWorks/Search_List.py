#!/usr/bin/python
#-*- coding: utf8 -*-

'''
function to search value on a list, receive two parameters list and value to search
'''

def pesquise(lis, value):
    for x,e in enumerate(lis):
        if e == value:
            return x
    return None

L = []

while True:
    V = int(input("Value: "))
    L.append(V)
    if V == 0:
        break
    
V_search = int(input("Search Value: "))
print(pesquise(L, V_search))

