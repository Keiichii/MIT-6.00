# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 11:09:44 2018

@author: ART
"""

def longestRun(L):
    tmp = 1
    ans = 1
    for idx in range(len(L[:-1])):
#        print(L[idx], L[idx+1])
        if L[idx] <= L[idx+1]:
            tmp += 1
            if tmp > ans:
                ans = tmp
        else:
            tmp = 1
    return ans


L = [10, 4, 6, 8, 3, 4, 5, 7, 7, 2, 3, 4]

print('Should return:', 5)
print(longestRun(L))