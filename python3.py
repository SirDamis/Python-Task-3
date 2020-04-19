from random import randint
print('How well can you guess? Welcome to the number guessing game.')
print('Levels avalaible:\n\tEasy\n\tMedium\n\tHard\
    \nEnter either easy or medium or hard as level.')

#A number guessing game
def level(max, times):
    number = randint(1, max)#generates random number between 1 and specify number
    print(f'You can only guess between 1 - {max}.')
    i = times
    try:
        while i > 0:    #Loop to execute the no of guesses
            print(f'You have {i} guess(es).')
            guess = int(input('Enter guess: '))
            if guess == number:
                print('You got it right!')
                break
            elif guess not in range(1,max+1): #Break if number is not within the range
                print(f'Number not between 1 to {max}')
                break
                
            else:
                print('You are wrong.')
                i = i -1
                if i == 0:
                    print('Game Over')
        print(f'Number is {number}')
                    
    except ValueError:
            print('Input a number')
            


def play():
    stage = input('Select level you want: ')
    if stage.lower() == 'easy':
        level(10, 6)
    elif stage.lower() == 'medium':
        level(20, 4)
    elif stage.lower() == 'hard':
        level(50,3)
    else:
        print('Incorrect input. Enter easy or medium or hard as level.')
        play()
play()