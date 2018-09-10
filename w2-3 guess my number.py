print('Please think of a number between 0 and 100!')
max = 100
min = 0
ans = (max-min)//2
while True:
    print('Is your secret number ' + str(ans) + '?', end='')
    x = input("Enter 'h' to indicate the guess is too high. Enter 'l' to \
indicate the guess is too low. Enter 'c' to indicate I guessed correctly.\n")
    if x == 'h':
        max = ans
    elif x == 'l':
        min = ans
    elif x == 'c':
        print('Game over. Your secret number was:', ans)
        break
    else:
        print('Sorry, I did not understand your input.')
    #print('max:', max, 'min:', min)
    ans = (max-min)//2+min

