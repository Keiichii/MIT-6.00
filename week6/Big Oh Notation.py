from math import log
c = 3

l = []
for x in range(1, 100):
    z = log(x)
    l.append(z)
print('logN', l)

l = []
for x in range(1, 100):
    l.append(x)
print('\nlinear', l)

l = []
for x in range(1, 100):
    l.append(x*log(x))
print('\nNlogN', l)

l = []
for x in range(1, 100):
    l.append(x**c)
print('\nnc', l)

l = []
for x in range(1, 100):
    l.append(c**x)
print('\ncn', l)