#A simple calculator made by The Echostar.

#Numbers
Num1 = int(input('Your first Number= '))
Num2 = int(input('Your second Number= '))

#Operator
Operator = input('Your Operator= ')
while Operator not in ['+', '-', '*', '/']:
  print('Unavailable or incorrect operator. Please try again.')
  Operator = input('Your Operator= ')

#Calculation
if Operator == '+':
  print(f'Your result is {Num1 + Num2} !')
elif Operator == '-':
  print(f'Your result is {Num1 - Num2} !')
elif Operator == '*':
  print(f'Your result is {Num1 * Num2} !')
else:
  print(f'Your result is {Num1 / Num2} !')
