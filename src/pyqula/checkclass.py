import collections
import numpy as np


# function to check if inputs are of certain type

def is_iterable(e): 
    try: 
       return isinstance(e, collections.Iterable)
    except: # workaround
       try: 
           iter(e)
           return True
       except: return False

def number2array(n,d=3):
    """Given a certain object, return an array"""
    if is_iterable(n): return [ni for ni in n]
    else: return [n for i in range(d)]
