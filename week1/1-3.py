s = 'azcbobobegghakl'

ans = tmp = s[0]
for prev_letter, letter in enumerate(s[1:]):
    print('if', s[prev_letter], '<', letter)
    if s[prev_letter] <= letter:
        tmp += letter
        print('tmp:', tmp)
        if len(tmp) > len(ans):
            ans = tmp
    else:
        tmp = letter
        print('tmp:', tmp)
    print('ans:', ans)

print('Longest substring in alphabetical order is:', ans)