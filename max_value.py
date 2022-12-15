#!/usr/bin/env python3

# Created by: Chris Di Bert
# Date: Dec.15, 2022
# This program generates 10 random numbers and
# prints the largest number

import random
import constants


def max_value(number_list):

    highest_number = -1

    # Gets the largest number by comparing previous largest numbers
    for counter in range(constants.MAX_ARRAY_SIZE):
        if number_list[counter] > highest_number:
            highest_number = number_list[counter]

    return highest_number


def main():
    # Creates an empty list to store the random numbers
    random_numbers = []

    # For loop generates ten random numbers from 1-100
    for counter in range(constants.MAX_ARRAY_SIZE):

        # Generates random number from 1-100
        random_int = random.randint(constants.MIN_NUM, constants.MAX_NUM)

        # Adds random number to list
        random_numbers.append(random_int)

        print(f"Added {random_int} to list at index {counter}")

    # Stores largest number generated in variable
    largest_value = max_value(random_numbers)

    # Prints the largest number generated
    print(f"The max value is: {largest_value}.")


if __name__ == "__main__":
    main()
