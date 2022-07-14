from itertools import product
import math
from art import *
print(logo)

print('### Welcome To Pycalulator ###')

#where uc = user choice

uc = int(input('>>>>Choose a calculation method<<<<\n1 -->> Addition\n2 -->> Substraction\n3 -->> Multiplication\n4 -->> Division\n5 -->> sqrts\n6 -->> AreaCalculator\n7 -->> BMI Index calculator\n8 -->> Percentage\nEnter Here--->>>>: '))

if uc == 1:
     print(sum(map(int, input("Enter the numbers you want to add(use space): ").split())))

if uc == 2:
    x = int(input('Enter a Number: '))
    y = int(input('Enter another Number: '))
    z = x-y
    print(z) 

if uc == 3:
    print(math.prod(map(int, input("Enter the numbers you want to Mutiplt(use space): ").split())))

if uc == 4:
    x = int(input('Enter a Number: '))
    y = int(input('Enter a Number you want to divide with: '))
    z = x//y
    r = x%y
    print('reminder',z)
    print('quotient',r)
    
if uc == 5:
    print(math.sqrt(int(input("Enter the number: "))))
    
if uc == 6:
    import Area
    
if uc == 7:
    import BMI

if uc == 8:
    x = int(input('Enter your number: '))
    y = int(input('Enter the total number: '))
    z = x/y*100
    print('Your percentage is: ',z)

