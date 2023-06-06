import random

def guess_number_ai(low, high):

    guess = random.randint(low, high)

    print(f"Is the number {guess}?")

    while True:

        response = input("Enter 'higher', 'lower', or 'correct': ").lower()

        if response == 'higher':

            low = guess + 1

            guess = random.randint(low, high)

            print(f"Is the number {guess}?")

        elif response == 'lower':

            high = guess - 1

            guess = random.randint(low, high)

            print(f"Is the number {guess}?")

        elif response == 'correct':

            print("Great! The AI guessed the number correctly.")

            break

        else:

            print("Invalid input. Please enter 'higher', 'lower', or 'correct'.")

def main():

    print("Welcome to the Number Guessing AI!")

    print("Think of a number and let the AI guess it.")

    low = int(input("Enter the lowest possible number: "))

    high = int(input("Enter the highest possible number: "))

    guess_number_ai(low, high)

if __name__ == '__main__':

    main()

