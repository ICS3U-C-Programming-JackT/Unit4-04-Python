#!/usr/bin/env python3
# Created By: Jack Turcotte
# Date: April 20, 2025

# Number guess loop program in python

import random


def main():

    # Initialize random number
    random_num = int(random.randrange(1, 10))

    while True:
        # Get user guess
        user_guess = input("Enter a random integer from 1 to 9: ")

        # Convert user guess to integer
        try:
            user_guess = int(user_guess)

            # Check if number is within the range, warn depending on the situation
            if user_guess > 0 and user_guess < 10:
                if user_guess == random_num:

                    # Break out of the loop to print the end msg
                    break
                else:

                    # Print incorrect
                    print("incorrect, please guess again")
            else:

                # Print incorrect
                print("The number you entered was out of range, please guess again")

        except:

            # Warn user that they entered string
            print("Please enter a valid integer. You entered ", user_guess)

    # Congratulate user
    print("You got it right! Thanks for playing!")

if __name__ == "__main__":
    main()
