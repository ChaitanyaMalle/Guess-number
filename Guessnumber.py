import random
import time

def intro():
    print("May I ask you for your name?")
    name = input("Enter your name: ")
    print(f"{name}, we are going to play a game. I am thinking of a number between 1 and 200")
    time.sleep(0.5)
    print("Go ahead. Guess!")
    return name

def pick(number, name):
    guesses_taken = 0
    while guesses_taken < 6:
        time.sleep(0.25)
        enter = input("Guess: ")
        try:
            guess = int(enter)
            if guess <= 200 and guess >= 1:
                guesses_taken += 1
                if guesses_taken < 6:
                    if guess < number:
                        print("The guess of the number that you have entered is too low")
                    if guess > number:
                        print("The guess of the number that you have entered is too high")
                    if guess!= number:
                        time.sleep(0.5)
                        print("Try Again!")
                if guess == number:
                    break
            else:
                print("Silly Goose! That number isn't in the range!")
                time.sleep(0.25)
                print("Please enter a number between 1 and 200")
        except ValueError:
            print("I don't think that " + enter + " is a number. Sorry")
    if guess == number:
        guesses_taken = str(guesses_taken)
        print(f'Good job, {name}! You guessed my number in {guesses_taken} guesses!')
    else:
        print(f'Nope. The number I was thinking of was {number}')

def main():
    play_again = "yes"
    while play_again.lower() == "yes" or play_again.lower() == "y":
        number = random.randint(1, 200)
        name = intro()
        pick(number, name)
        print("Do you want to play again?")
        play_again = input()

if __name__ == "__main__":
    main()