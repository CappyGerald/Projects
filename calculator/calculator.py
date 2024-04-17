from sys import exit
from textwrap import dedent

'''
A simple calculator project to enhance an 
understanding of the following concepts:

1. Functions
2. Math operations in python
3. user inputs
4. Operators in python
5. Handling errors in python

'''
# let's start by defining different
# functions to perform different mathematical operations


def add(a, b):
    """takes in two integers as arguments and adds them"""
    return a + b

def subtract(a, b):
    """takes in two integers as arguments and subtracts them"""
    return a - b

def multiply(a, b):
    "takes in two integers as arguments and multiplies them"""
    return a * b

def divide(a, b):
    """takes in two integers as arguments and divides them"""
    
    if b != 0:
            return a // b
    else:
         print("Can't divide by Zero!")
         
def calculate():
    try: 
        while True:
            display_info()
            num1 = float(input("Enter the first number:\n"))
            op = input('Enter an operator:\n')
            num2 = float(input("Enter the second number:\n"))
            if op == '+':
                result = add(num1, num2)
                print("result is", result)
                return result
                
            elif op == '-':
                result = subtract(num1, num2)
                print("result is", result)
                return result
                
            elif op == '/':
                result = divide(num1, num2)
                print("result is", result)
                return result 
            
            
            elif op == '*':
                result = multiply(num1, num2)
                print("result is", result)
                return result
            else:
                print("Invalid operator!")
    except ValueError:
        print("Enter a valid number!")
def display_info():
    """
    Displays info about the calculator
    """
    info = dedent("""
           This is a simple calculator which is capabale of carrying
           basic mathematical computation.
           Enter the following operators:
           + : for addition
           - : for subraction
           * : for multliplication
           / : for addition

           future versions may be extended to carryout more operations.
         """)
    print(info)


calculate()