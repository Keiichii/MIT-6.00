def genPrimes():
    natural = 1
    while True:
        natural +=1
        n = natural-1
        x = 0
        while n>1:
            if natural%n == 0:
                x =1
                break
            n-=1
        if x == 0:
            yield natural
            
x = genPrimes()
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
