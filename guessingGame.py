#!usr/bin/env python
import sys
import random


def takeInput():
    highest = sys.argv[1]
    while True:
        try:
            if int(highest) > 10:
                break
            else:
                highest = raw_input("please enter range ceiling (integer) greater than 10, or type 'quit' to quit: ")
                if highest == 'quit':
                    print('exiting...')
                    return
        except:
            highest = raw_input("please enter range ceiling (integer) greater than 10, or type 'quit' to quit: ")
            if highest == 'quit':
                print('exiting...')
                return
    highest = int(highest)
    answer = random.randint(0,highest + 1)
    hi_ans = []
    hi_ans.append(highest)
    hi_ans.append(answer)
    return hi_ans

def playGame(highest, answer):
    guess = raw_input("Guess a number from 0 to %d, or type 'quit' to quit: " %highest)
    if guess == 'quit':
        print('exiting...')
        return
    prev_guess = int(guess)
    guess = int(guess)
    while guess > highest or guess < 0:
        if guess == 'quit':
            print('exiting...')
            return
        elif int(guess) > highest:
            guess = raw_input("please guess a number within the bounds, or type 'quit' to quit: ")
            if guess == 'quit':
                    print('exiting...')
                    return
            guess = int(guess)
            if int(guess) == prev_guess:
                guess = raw_input("please guess a number not previously guessed, or type 'quit' to quit: ")

        else:
            guess = raw_input("please guess a number within the bounds, or type 'quit' to quit: ")
            if guess == 'quit':
                print('exiting...')
                return
            guess = int(guess)
            if guess == prev_guess:
                guess = raw_input("please guess a number not previously guessed, or type 'quit' to quit: ")
                if guess == 'quit':
                    print('exiting...')
                    return
            guess = int(guess)
    while int(guess) != answer:
        if(int(guess) < answer):
            print("answer is higher")
            guess = raw_input("Guess a number from 0 to %d, or type 'quit' to quit: " %highest)
            if guess == 'quit':
                    print('exiting...')
                    return
            while int(guess) == prev_guess:
                guess = raw_input("please guess a number not previously guessed, or type 'quit' to quit: ")
            guess = int(guess)
            while guess > highest or guess < 0:
                if guess == 'quit':
                    print('exiting...')
                    return
                elif int(guess) > highest:
                    guess = raw_input("please guess a number within the bounds, or type 'quit' to quit: ")
                    if int(guess) == prev_guess:
                        guess = raw_input("please guess a number not previously guessed, or type 'quit' to quit: ")
                    elif guess == 'quit':
                            print('exiting...')
                            return
                    guess = int(guess)
                else:
                    guess = raw_input("please guess a number within the bounds: ")
                    if int(guess) == prev_guess:
                        guess = raw_input("please guess a number not previously guessed, or type 'quit' to quit: ")
                        if guess == 'quit':
                            print('exiting...')
                            return
        else:
            print("answer is lower")
            guess = raw_input("Guess a number from 0 to %d, or type 'quit' to quit: " %highest)
            if guess == 'quit':
                    print('exiting...')
                    return
            while int(guess) == prev_guess:
                guess = raw_input("please guess a number not previously guessed, or type 'quit' to quit: ")
                if guess == 'quit':
                        print('exiting...')
                        return
            guess = int(guess)
            while guess > highest or guess < 0:
                if guess == 'quit':
                    print('exiting...')
                    return
                elif guess > highest:
                    guess = raw_input("please guess a number within the bounds, or type 'quit' to quit: ")
                    if int(guess) == prev_guess:
                        guess = raw_input("please guess a number not previously guessed, or type 'quit' to quit: ")
                    elif guess == 'quit':
                            print('exiting...')
                            return
                else:
                    guess = raw_input("please guess a number within the bounds: ")
                    if int(guess) == prev_guess:
                        guess = raw_input("please guess a number not previously guessed, or type 'quit' to quit: ")
                        if guess == 'quit':
                            print('exiting...')
                            return
    print("you've guessed it! the answer is %d." %answer)


##================== MAIN ===================

if __name__ == '__main__':
    hi_ans = takeInput()
    wantLoop = True
    highest = int(hi_ans[0])
    answer = int(hi_ans[1])
    while wantLoop:
        if highest >= answer and answer >= 0:
            wantLoop = False
        else:
            if highest < answer:
                answer = int(raw_input("answer was higher than the limit, please enter a new one, or type 'quit' to quit: "))
                if answer == 'quit':
                    print('exiting...')
                    wantLoop = False
            else:
                answer = raw_input("answer %d was negative, please enter a new one, or type 'quit' to quit: " %answer)
                if answer == 'quit':
                    print('exiting...')
                    wantLoop = False
    if answer != 'quit':
        playGame(int(highest), int(answer))
