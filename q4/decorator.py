#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: github.com/maliozer
@license: MIT
"""


##main idea behind the  decorator
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

def say_whee():
    print("Whee!")

say_whee = my_decorator(say_whee)

@my_decorator
def dev():
    print("Hello")


#%%
    
def smart_divide(func):
    def wrapper(*args, **kwargs):
        if(args[1] == 0):
            print("Whoops! cannot divide")
        else:
            func(*args, **kwargs)
    return wrapper

@smart_divide
def divide(a,b):
    print(a/b)




