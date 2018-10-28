# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 11:26:10 2018

@author: ART
"""

def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    set1, set2 = set(d1), set(d2)
    
    #intersect
    #The keys to the intersect dictionary are keys that are common in both d1 and d2. To get the values of the intersect dictionary, look at the common keys in d1 and d2 and apply the function f to these keys' values
    intersect = set1.intersection(set2)
    intersect_result = {}
    for key in intersect:
        intersect_result[key] = f(d1[key], d2[key]) 
       
    #difference
    #a key-value pair in the difference dictionary is (a) every key-value pair in d1 whose key appears only in d1 and not in d2 and (b) vesa versa
    difference_result = {}
    difference = set1.difference(set2).union(set2.difference(set1))
    for key in difference:
        if key in d1:
            difference_result[key] = d1[key]
        else:
            difference_result[key] = d2[key]
    return (intersect_result, difference_result)
   
# CASE 1
d1 = {1:30, 2:20, 3:30, 5:80}
d2 = {1:40, 2:50, 3:60, 4:70, 6:90}

def f(a, b):
    #print(a, 'type:', type(a))
    #print(a+b, 'type:', type(a+b))
    return a+b
    
print('#CASE 1\nShould return: ({1: 70, 2: 70, 3: 90}, {4: 70, 5: 80, 6: 90})')
print(dict_interdiff(d1, d2))

# CASE 2
d1 = {1:30, 2:20, 3:30}
d2 = {1:40, 2:50, 3:60}

def f(a, b):
    return a>b

print('#CASE 2\nShould return: ({1: False, 2: False, 3: False}, {})')
print(dict_interdiff(d1, d2))
