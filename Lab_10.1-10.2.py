"""

Create a Python file named lab_10-1.py
*** You must write a comment for every chunk of code you write from now on along with your author tag***

Using a while loop, write a program that prompts the user to input a number.
If the user inputs a number, add that to the sum of the previous numbers entered.
If the user enters -1, the program should end and display the sum of all the numbers entered.
Be sure the program uses a break statement
_____________________________________________________________________________________________________________

Create a Python file named lab_10-2.py
Using the same approach as lab 1, write a program that prints all the numbers that are multiples of 3 in a list. Be sure your program uses a continue statemen


"""

# Author: Alsir Elsheikh
# This program uses a while loop to continuously prompt the user for input.
# It adds the entered numbers to a running sum until the user inputs -1, which breaks out of the loop.
# Finally, it displays the sum of all the numbers entered.

sum_of_numbers = 0

while True:
    user_input = input("Enter a number (or -1 to exit): ")

    # Check if the user entered -1 to exit the loop
    if user_input == "-1":
        break

    # Check if the user input is a valid number
    if user_input.isdigit():
        number = int(user_input)
        sum_of_numbers += number
    else:
        print("Invalid input. Please enter a valid number.")

# Display the sum of all entered numbers
print(f"Sum of all numbers entered: {sum_of_numbers}")

# Author: Alsir Elsheikh

# This program prints all the numbers that are multiples of 3 in a given list.
# It uses a continue statement to skip printing numbers that are not multiples of 3.

numbers_list = [1, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30]

print("Multiples of 3 in the list:")

for num in numbers_list:
    # Check if the number is not a multiple of 3
    if num % 3 != 0:
        continue

    # If the number is a multiple of 3, print it
    print(num)

