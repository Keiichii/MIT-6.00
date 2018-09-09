s = 'azcbobobegghakl'

w = 'bob'
ans = 0
start = 0
stop = 3
while stop < len(s)+1:
    if s[start: stop] == w:
        ans +=1
    start +=1
    stop +=1
    
print('Number of times bob occurs is:', ans)