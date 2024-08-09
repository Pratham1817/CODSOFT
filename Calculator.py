def addition(num1,num2):
    return num1+num2

def subtraction(num1,num2):
    return num1-num2

def multiplication(num1,num2):
    return num1*num2

def division(num1,num2):
    return num1/num2

print("SELECT YOUR OPERATION")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")


operation=int(input("SELECT OPERATION 1/2/3/4:"))

num1=float(input("Enter First Number:"))
num2=float(input("Enter Second Number:"))

if operation==1:
    print(num1,"+",num2,"=",addition(num1,num2))

elif operation==2:
    print(num1,"-",num2,subtraction(num1,num2))

elif operation==3:
    print(num1,"*",num2,"=",multiplication(num1,num2))

elif operation==4:
    print(num1,"/",num2,"=",division(num1,num2))

else:print("Please Enter Valid Input")