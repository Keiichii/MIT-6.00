def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements. Remaining elements in L
            should be in the same order.
    Returns the length of L after mutation
    """
    ans =list(filter(f, L))
    def ch(l):
        global L
        L = l
        return(len(L))
    return ch(ans)
    
L = ['a', 'b', 'c', 'a','b','a']
def f(s):
        vowels = ['a', 'c','d']
        return s in vowels

print(satisfiesF(L))
print(L)

