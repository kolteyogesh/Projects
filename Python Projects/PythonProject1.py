print('*************   CALCULATOR     ****************')
def add(num1,num2):
    return num1 + num2
def sub(num1,num2):
    return num1 - num2
def mul(num1,num2):
    return num1*num2
def divide(num1,num2):
    return num1/num2
def mod(num1,num2):
    return num1%num2
choice = input('Enter choice(1,2,3,4): ')
num1 = float(input('Enter first number:  '))
num2 = float(input('Enter second number: '))
if choice == '1':
    res = add(num1,num2)
    print('Addition =',res)
    #print('Addition: ',num1,'+',num2,'=',res)
elif choice == '2':
    res = sub(num1,num2)
    print('Subtraction =',res)
    #print('Subtraction: ',num1,'-',num2,'=',sub(num1,num2))
elif choice == '3':
    res = mul(num1,num2)
    print('Multiplication =',res)
    #print('Multiplication: ',num1,'*',num2,'=',mul(num1,num2))
elif choice == '4':
    res = divide(num1,num2)
    print('Division =',res)
    #print('Division: ',num1,'/',num2,'=',divide(num1,num2))
elif choice == '5':
    res = mod(num1,num2)
    print('Modulus =',res)
    #print('Modulus: ',num1,'%',num2,'=',mod(num1,num2))
else:
    print('Invalid input')
