#!/usr/bin/env python3
# Created By: Jack Turcotte
# Date: April 20, 2025

# Number guess loop program in python

import random


def main():

    random_num = int(random.randrange(1, 10))

    while True:
        user_guess = input("Enter a random integer from 1 to 9: ")

        try:
            user_guess = int(user_guess)

            if user_guess > 0 and user_guess < 10:
                if user_guess == random_num:
                    break
                else:
                    print("incorrect, please guess again")
            else:
                print("The number you entered was out of range, please guess again")

        except:
            print("Please enter a valid integer. You entered ", user_guess)
    print("You got it right! Thanks for playing!")


if __name__ == "__main__":
    main()
