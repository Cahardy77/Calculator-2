"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

user_input = ""
while user_input != "q":
    user_input = input("User input: ")
    user_input = user_input.split(" ")
    if len(user_input) < 2:
        print("not enough numbers")
        continue
    operator = user_input[0]
    first_num = user_input[1]
    if len(user_input) < 3:
        second_num= "0"
    else:
        second_num= user_input[2]

    result=None

    if operator == "+":
        result=add(float(first_num),  float(second_num))
    elif operator == "-":
        result=subtract(float(first_num),  float(second_num))
    elif operator == "/":
        result=divide(float(first_num),  float(second_num))
    elif operator == "*":
        result=multiply(float(first_num),  float(second_num))
    elif operator == "square":
        result=square(float(first_num),  float(second_num))
    elif operator == "cube":
        result=cube(float(first_num))
    elif operator == "power":
        result=power(float(first_num),  float(second_num))
    elif operator== "mod":
        result=mod(float(first_num),  float(second_num))
        
    print(result)

    
    
    
        




