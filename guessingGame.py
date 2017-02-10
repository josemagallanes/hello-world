import random
# Guessing Game: A very simple guessing game

def main():
    number = random.randint(0,10)
    guess = input("Enter a number between 0 and 10: ")
    while (guess != str(number)):
        guess = input("Wrong answer! Please try again: ")
    print("Correct! The number was", number)
main()