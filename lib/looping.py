#!/usr/bin/env python3

def happy_new_year():
    i = 10  # Start counting from 10
    while i >= 1:  # Continue looping as long as i is greater than or equal to 1
        print(i)  # Print the current value of i
        i -= 1  # Decrement i by 1
    print("Happy New Year!")  # Print "Happy New Year!" after the loop ends


def square_integers(int_list):
    return [num ** 2 for num in int_list]  # Square each number in the list


def fizzbuzz():
    for i in range(1, 101):  # Loop through numbers 1 to 100
        if i % 3 == 0 and i % 5 == 0:  # Check if divisible by both 3 and 5
            print("FizzBuzz")
        elif i % 3 == 0:  # Check if divisible by 3
            print("Fizz")
        elif i % 5 == 0:  # Check if divisible by 5
            print("Buzz")
        else:  # If none of the above, print the number
            print(i)

     # Main execution block
if __name__ == "__main__": 
    print("Testing happy_new_year():")
    happy_new_year()

    print("\nTesting square_integers([1, 2, 3, 4, 5]):")
    print(square_integers([1, 2, 3, 4, 5]))

    print("\nTesting fizzbuzz():")
    fizzbuzz()   