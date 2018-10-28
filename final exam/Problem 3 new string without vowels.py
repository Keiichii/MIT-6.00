def print_without_vowels(s):
    new_s = s
    vowels = [ 'a', 'e', 'i', 'o', 'u']
    for letter in vowels:
        if letter in new_s:
            new_s = new_s.replace(letter, '')
            new_s = new_s.replace(letter.upper(), '')
    print(new_s)
    
s = "This is great!"
print(print_without_vowels(s))