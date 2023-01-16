"""
Program: Simple Calculator 
Author: Anas Tawalbeh
Simple calcuatro help the user calculate the basic 4 operations including:
addition, subtraction, multiplication and division
Significant constants
         there is no constants
 2. The inputs are
         2 numbers (at least)
 3. Computations:
         addition: number + another number
         subtraction: number - another number
         multiplication: number * another number
         division: number / another number
 4. The outputs are
         computation result
"""
import sys
number1= number2= result= 0
operator=''

def addition():
    global number1, number2
    result=number1+number2
    print(f"The sumation for the two values is equal to: {result}")
def subtraction():
    global number1, number2
    result=number1-number2
    print(f"The sumation for the two values is equal to: {result}")
def multiply():
    global number1, number2
    result=number1*number2
    print(f"The sumation for the two values is equal to: {result}")
def divide():
    global number1, number2
    result=number1/number2
    print(f"The sumation for the two values is equal to: {result}")
def again():
    calc_again = input('''
    Do you want to calculate again?
    Please type Y for YES or N for NO.
    ''')
    if calc_again.upper() == 'Y':
        main()

    elif calc_again.upper() == 'N':
        sys.exit('See you later.')
    else:
        again()
def validate_input():
    global number1
    try:
        number1=float(input("Insert the first value\n"))
    except:
        print("Your first input is not a number\n")
        validate_input()
def validate_second_input():
    global number2
    try:
        number2=float(input("Insert the second value\n"))
    except:
        print("Your first second is not a number\n")
        validate_second_input()
def validate_operator():
    operator = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
''')
    if operator =='+':
        validate_input()
        validate_second_input()
        addition()
    elif operator =='-':
        validate_input()
        validate_second_input()
        subtraction()
    elif operator =='*':
        validate_input()
        validate_second_input()
        multiply() 
    elif operator =='/':
         validate_input()
         validate_second_input()
         divide()
    else:
        print("Invalid operator\n")
        validate_input()
        validate_second_input()
        validate_operator()
def main():
    validate_operator()
    again()
        
                
if __name__ == "__main__":
    main()
       
