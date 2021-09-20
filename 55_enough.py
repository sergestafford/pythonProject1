number = 0
count = 1 
a = []

while number != 55:
  number = int(input())
  a.append(number)
  if number == 55:
    summa = sum(a[:-1])
    r = round(summa // (count - 1))  
    print(count - 1)
    print(summa)
    print(r)
  count += 1



"""Write a program that reads numbers until a user enters 55. 
Once 55 is entered, stop reading the input, print out how many numbers have been entered, 
their total sum, and average (do the rounding this way: round(number)). 
Do NOT include 55 in your calculations and print each resulting value on a new line 
in the order given above."""