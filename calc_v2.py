import math

run = True

while run:
    a = float(input())
    b = float(input())
    c = input()
    if math.inf > a or b > -math.inf:
        if c == "+":
            print(a + b)
        elif c == "-":
            print(a - b)
        elif c == "/": 
            try: 
                print(a / b)
            except ZeroDivisionError: 
                print("Division by 0!")
        elif c == "*":
            print(a * b)
        elif c == "mod":
            try:
                print(a % b)
            except ZeroDivisionError: 
                print("Division by 0!")
        elif  c == "pow":
            print(a ** b)
        elif c == "div":
            try: 
                print(a // b)
            except ZeroDivisionError: 
                print("Division by 0!")
        else:
            print("Wrong action.")
