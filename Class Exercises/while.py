secretNumber = 9

while True:

    guess = float(input('Guess the number: '))

    if(guess == secretNumber):
        break
    
    if(guess > secretNumber):
        print('Too high!')
    else:
        print('Too low!')

print('You guessed it!')

##
##tokens = 40
##
##while True:
##    subToken = int(input('How many tokens do you want to use: '))
##    tokens -= subToken
##
##    if(tokens < 0):
##        print('You don\'t have enough tokens left')
##        break
##    print('You have ' + str(tokens) + ' tokens left.')
##
