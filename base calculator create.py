#Create a console base calculator.

num1=eval(input("enter your first number:-"))
num2=eval(input("enter your second number:-"))
operation=input(''' '+' for addition, '-' for sub, '*' for multiplication, '/' for division''')
if operation=='+':
    output= num1+num2
    print(output)
if operation=='-':
    output=num1-num2
    print(output)
if operation=='*':
    output= num1*num2
    print(output)
if operation=='/':
    output=num1/num2
    print(output)

    



