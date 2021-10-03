# write your code here
import math
import argparse
import sys

P = 0  # loan_principal
A = 0  # monthly_payment (diff or annuity)
i = 0  # loan_interest
n = 0  # number_of_payments

parser = argparse.ArgumentParser()
parser.add_argument("--type")
parser.add_argument("-P", "--principal")
parser.add_argument("-A", "--payment") 
parser.add_argument("-n", "--periods")
parser.add_argument("-i", "--interest")

args = parser.parse_args()

options = [args.type, args.principal, args.payment, args.periods, args.interest]

def options_num(options):
    j = str('Incorrect parameters')
    if len(options) < 4:
        print(j)
        sys.exit()
    elif args.type == None:
        print(j)
        sys.exit()
    elif args.type == 'diff' and args.payment != None:
        print(j)
        sys.exit()
    elif args.interest == None:
        print(j)
        sys.exit()
    elif args.periods == None and args.interest == None:
        print(j)
        sys.exit()
options_num(options)

if args.type == 'diff':
    P = args.principal
    n = args.periods
    i = args.interest
    P = float(P)
    n = int(n)
    i = float(i)
    i = i / (12 * 100)
    c = 1
    m = 1
    s = 0
    for c in range(c, n + 1):
        m = c
        x = ((P * (m - 1)) / n)
        A = (P / n) + (i * (P - x)) 
        A = math.ceil(A)
        s += A
        print('Month', c,':', 'payment is', A)
        c += 1
    print()
    print('Overpayment =', math.ceil(s - P))

if args.type == 'annuity' and args.periods == None:
    P = args.principal
    A = args.payment
    i = args.interest
    P = float(P)
    A = float(A)
    i = float(i)
    i = i / (12 * 100)
    x = (A / (A - i * P))
    base = 1 + i
    n = math.log(x, base)
    n1 = n / 12
    n1 = math.ceil(n1)
    if n % 12 != 0:
        n2 = int(n // 12)
        n3 = math.ceil(365 * (n / 12 - n // 12) / 30)
        if n3 == 12:
            print('It will take', n2 + 1, 'years to repay this loan!')
            print()
            print('Overpayment =', math.ceil(A * (n2 + 1) * 12 - P))
        elif n3 == 1:
            print('It will take', n2, 'years and', n3, 'month to repay this loan!')
            print()
            print('Overpayment =', math.ceil(A * (n2 * 12 + n3) - P))
        elif n3 > 1:
            print('It will take', n2, 'years and', n3, 'months to repay this loan!')
            print()
            print('Overpayment =', math.ceil(A * (n2 * 12 + n3) - P))
    elif n % 12 == 0:
        if n1 == 1:
            print('It will take', n1, 'year to repay this loan!')
            print()
            print('Overpayment =', math.ceil(A * n1 * 12 - P))
        elif n1 != 1:
            print('It will take', n1, 'years to repay this loan!')
            print()
            print('Overpayment =', math.ceil(A * n1 * 12 - P))

if args.type == 'annuity' and args.payment == None:
    P = args.principal
    n = args.periods
    i = args.interest
    P = float(P)
    n = int(n)
    i = float(i)
    i = i / (12 * 100)
    i_n = (1 + i) ** n
    A = P * ((i * i_n) / (i_n - 1))
    A = math.ceil(A)
    print('Your monthly payment =', A,end='!')
    print('\n')
    print('Overpayment =', math.ceil(A * n - P))

if args.type == 'annuity' and args.principal == None:
    A = args.payment
    n = args.periods
    i = args.interest
    A = float(A)
    n = int(n)
    i = float(i)
    i = i / (12 * 100)
    i_n = (1 + i) ** n
    P = A / (i * i_n / (i_n - 1))
    P = round(P)
    print('Your loan principal =', P,end='!')
    print('\n')
    print('Overpayment =', math.ceil(A * n - P))