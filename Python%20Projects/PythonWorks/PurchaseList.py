#!/usr/bin/env python
#-*- coding: utf8 -*-

'''
Created on 24 de ago de 2016

@author: Mauro Cesar de Oliveira
'''

'''
This program create and print a purchase list,
only using a python list
'''

#enter a empty list
purchase = []

while True:
    product = input("Product: ")
    if product == "end":
        break
    quantity = int(input("Quantity: "))
    price = float(input("Price: "))
    #create lists inside list
    purchase.append([product, quantity, price])
#this sum_ is just to differentiate to sum, that is a reserved word of python
sum_ = 0.0

for e in purchase:
    print("%20s x%5d %5.2f %6.2f" % (e[0], e[1], e[2], e[1] * e[2]))
    sum_ += e[1] * e[2]
print("Total: %7.2f" % sum_)     
