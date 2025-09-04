'''
Question 1

Write a Python program that works as a basic calculator with continuous use.

Instruction
    The program should repeatedly allow the user to perform operations until they choose to exit.
    Ask the user to enter two numbers.
    Then ask them to choose an operation: addition, subtraction, multiplication, or division.
    Use functions to define each operation.
    Use try-except to handle invalid input and division by zero.
    Use control flow (if-elif-else) to select the correct operation.
    Use a while loop to keep running until the user chooses to exit.
'''


def add(x, y):
    return (f'Result: {x + y}\n')


def subtract(x, y):
    return (f'Result: {x - y}\n')


def multiply(x, y):
    return (f'Result: {x * y}\n')


def divide(x, y):
    try:
        return (f'Result: {x / y}\n')
    except ZeroDivisionError:
        return "Error: Cannot divide by zero. \n"


def calculator():
    while True:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        choice = input("Choose operation (+, -, *, /) or 'exit' to quit: ")

        if choice == 'exit':
            print("Exiting the calculator. Goodbye!")
            break

        if choice == '+':
            print(add(num1, num2))
        elif choice == '-':
            print(subtract(num1, num2))
        elif choice == '*':
            print(multiply(num1, num2))
        elif choice == '/':
            result = divide(num1, num2)
            print(result)
        else:
            print("Invalid choice. Please select a valid operation.")

calculator()


"""Question 2

    Complete the missing parts of the program below so that it keeps asking the user for a number and tells whether it is even or odd.

Instruction

    Use input, int conversion, if-else control flow, and print output.
    Use a while loop that runs until the user types 'exit'.

"""

while True:
    user_input = input("Enter a number (or type 'exit' to quit): ")
    if user_input == "exit":
        print("Goodbye!")
        break        # break out of loop
    try:
        num = int(user_input)   # convert to integer
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue
    if num % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")


"""Question 3
    The following code is supposed to ask for a user’s age repeatedly and say whether they are allowed to vote (18+).
    It should also exit if the user types 'exit'. However, the code contains errors.
"""

while True:
    age = input("Enter your age (or type exit to quit): ")
    if age == "exit":
        print("Goodbye!")
        break
    try:
        age = int(age)
        if age >= 18:
            print("You can vote")
        else:
            print("You cannot vote")
    except:
        print("Invalid input")