import random
# Guessing Game: A very simple guessing game

def main():
    number = random.randint(0,10)
    print(number) #DELETEME
    guess = input("Enter a number between 0 and 10: ")
    print(guess) #DELETEME
    while (guess != str(number)):
        guess = input("Wrong answer! Please try again: ")
    print("Correct! The number was", number)


main()