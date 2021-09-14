import math

run = True

while run:
  a = float(input("Введите число: "))
  b = float(input("Введите второе число: "))
  c = input("Введите действие: ")

  if (math.inf > a > -math.inf or math.inf > b > -math.inf) and c == "+":
    print(a + b)
  elif (math.inf > a > -math.inf or math.inf > b > -math.inf) and c == "-":
    print(a - b)
  elif (math.inf > a > -math.inf or math.inf > b > -math.inf) and c == "/": 
    try: 
      print(a / b)
    except ZeroDivisionError: 
      print("Деление на 0!")
  elif (math.inf > a > -math.inf or math.inf > b > -math.inf) and c == "*":
    print (a * b)
  elif (math.inf > a > -math.inf or math.inf > b > -math.inf) and c == "%":
    try:
      print(a % b)
    except ZeroDivisionError: 
      print("Деление на 0!")
  elif (math.inf > a > -math.inf or math.inf > b > -math.inf) and c == "**":
    print(a ** b)
  elif (math.inf > a > -math.inf or math.inf > b > -math.inf) and c == "//":
    try: 
      print(a // b)
    except ZeroDivisionError: 
      print("Деление на 0!")
  else:
    print("Неверное действие.")
