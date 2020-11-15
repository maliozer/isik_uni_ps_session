#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: github.com/maliozer
@license: MIT
"""

import threading
import time


def meow():
    print('MEOWWWW!!!')
    time.sleep(2)
    print('MEOWWWW!!!')

def havv():
    print("Havv Havvv!!")
    time.sleep(3)
    print("Hırrr!!")
    

#%%
    
#calling without thread

start = time.perf_counter()

meow()
havv()

finish = time.perf_counter()

print(f'Finished in {round(finish-start,2)} seconds(s)')

#%%

#calling with thread

start = time.perf_counter()

t1 = threading.Thread(target=meow)
t2 = threading.Thread(target=havv)

t1.start()
t2.start()

t1.join()
t2.join()

finish = time.perf_counter()

print(f'Finished in {(finish-start,2)} seconds(s)')