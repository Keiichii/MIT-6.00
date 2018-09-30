def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements
    Returns the length of L after mutation
    """
    newList = L[:]
    for i in newList:
        if f(i)==False:
            L.remove(i)
    return len(L)

# For testing only, remove before submitting
def f(s):
    return 'a' in s

L = ['a', 'b', 'c', 'a','b','a']
def f(s):
        vowels = ['a', 'c','d']
        return s in vowels

print(satisfiesF(L))
print(L)
