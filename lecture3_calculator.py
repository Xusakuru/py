print("Welcome to the python calculator")
num1 = input("enter the first number:")
num2 = input("enter the second number:")
calculation = input("enter the basic arithmetic you want to calculate in:")


if calculation == '*':
      answer_1 = int(num1) * int(num2)
      print('the answer is %d' % (answer_1))

if calculation == ('/'):
      answer_2 = int(num1) / int(num2)
      print('the answer is %d' % (answer_2))

if calculation == ('+'):
      answer_3 = int(num1) + int(num2)
      print('the answer is %d' % (answer_3))

if calculation == '-':
      answer_4 = int(num1) - int(num2)
      print('the answer is %d' % (answer_4))


else:

      print("wrong answer")











