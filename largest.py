num1=int(input("Enter the first number: "))
num2=int(input("Enter second number: "))
num3=int(input("Enter the third number: "))
if(num1>num2) and (num1>num3):
    biggest=num1;
elif (num2>num1) and (num2>num3):
    biggest=num2;
else:
    biggest=num3;
print("The largest number is",biggest);
