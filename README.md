# Ai-number-guesser
In this AI tool, the program prompts the user to think of a number within a specified range. The AI will then make initial random guesses within that range. Based on the user's feedback of "higher," "lower," or "correct," the AI will adjust its guesses accordingly until it guesses the correct number.

The guess_number_ai function takes a low and high range as inputs. It generates a random guess within that range and prompts the user to provide feedback. If the user responds with "higher," the function updates the low range to be one more than the previous guess. If the user responds with "lower," the function updates the high range to be one less than the previous guess. If the user responds with "correct," the function ends the game.

The main function initiates the game by taking the lowest and highest possible numbers from the user and then calling the guess_number_ai function to start the AI's guessing process.
