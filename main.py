# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
def say_hi():
    return 'Hello and welcome to my program'
print(say_hi())

# Press the green button in the gutter to run the script.
#In Python, we use square brackets ([ ]) when defining a lis

# Basic addition function


# Program make a simple calculator

# This function adds two numbers
def add(x, y):
    return x + y


# This function subtracts two numbers
def subtract(x, y):
    return x - y


# This function multiplies two numbers
def multiply(x, y):
    return x * y


# This function divides two numbers
def divide(x, y):
    return x / y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            break

    else:
        print("Invalid Input")


# Found this at https://pastebin.com/w22EJ84n
# Run, assess then correct
# Add try and except blocks to your calculator program
# to handle these possible exceptions:
# The user tries to divide by zero.
# The user inputs non-numeric values.
# The user inputs an invalid option from the list of operations.
# Restructure your program where necessary. For example, if you used if else code blocks to check if the user attempts to divide by zero, try to convert this feature into a try and except block instead

# THIS IS SECOND CALCULATOR ATTEMPT THAT IS OPERATIONAL

# Print main menu
# Main menu
# + addition
# - subtraction
# * multiplication
# / division
# m show this menu
# q quit
def print_main_menu():
    print(' Main menu:')
    print('+ addition')
    print('- subtraction')
    print('* multiplication')
    print('/ division')
    print('m show this menu')
    print('q quit')


# Input a number
def input_number(prompt):
    # prompt: string
    # returns coder, number
    #  code=0: quit
    #  code=1: return to main menu
    #  code=2: the number has been input
    while True:
        input_string = input(prompt)
        if input_string:
            if input_string == "q":
                return 0, None  # q
            else:  # number was expected
                try:
                    number = float(input_string)
                except ValueError:  # non-empty string, neither "q" nor a number
                    print('That is not a number.')
                    print('Enter an empty line to return to the main menu, or enter "q" to quit.')
                else:
                    return 2, number  # number was input
        else:
            return 1, None  # empty string


# The following functions are for binary operations
# They return number in case of success, and an error string in case of error
def cfun2_addition(x, y):
    return x + y


def cfun2_subtraction(x, y):
    return x - y


def cfun2_multiplication(x, y):
    return x * y


def cfun2_division(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        return "Division by zero is not possible"
    return result
























































