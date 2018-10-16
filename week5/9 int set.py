# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 09:57:55 2018

@author: usov
"""

class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self""" 
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'
    
    def intersect(self, other):
        """
        returns a new intSet containing elements that appear in both sets. 
        In other words,
        
        s1.intersect(s2) return a new intSet of integers that appear in both s1 and s2.
        """
        z = intSet()
        for x in self.vals:
            if other.member(x):
                z.insert(x)
        return z
    
    def __len__(self):
        "that len(s) returns the number of elements in s"
        return len(self.vals)


a = intSet()
a.insert(1)
a.insert(2)
a
print('a', a)

b = intSet()
b.insert(3)
b.insert(1)
print('b', b)

c = a.intersect(b)
print('c', c)
print('a', a)

print('len:', len(a), len(b), len(c))