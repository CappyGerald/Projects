from textwrap import dedent
from sys import exit


GREETING = dedent("""
    Hello. This a basic Body Mass 
    Index calculator.
    Enter your weight and 
    height to know yours.
          """)

print(GREETING)

def calculate_bmi():
    """Computes User's BMI.
       Returns a float.
    """
    try: 
        weight = float(input("Enter weight in Kg:\n"))
        height = float(input("Enter weight in Metres:\n"))
        return weight / (height ** 2)
    except ValueError:
        print("Enter a valid number!")
    except ZeroDivisionError:
        print("Can't divide a number with Zero!")
def main():
    "Main logic of our programme." 
    name = input("Enter your name:").capitalize()
    result = calculate_bmi() 
    if result < 18.5:
        print(f"Hey, {name},your BMI is {result}")
        print("You're underweight.You need to gain more")
    elif 18.5 < result< 29.5:
        print(f"hey {name}, your BMI is {result}.")
        print("Your BMI is normal. Congratulations!")
    else:
        print(f"Hey {name}, Your BMI is {result}.")
        print("You're overweight.\n")

    print("Do you wan't to recalculate again?")
    response = input("yes/no?\n").lower()
    if response.startswith('y'):
        main()
    else:
        print("You've chosen not to recalculate.")
        print("Exiting...")
        exit(0)


if __name__ == '__main__':
    main()