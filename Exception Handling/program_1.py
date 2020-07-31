a = int(input("Enter First number:"))
b = int(input("Enter Second number:"))
try:
    res = a//b
    print("result is: ",res)
except ZeroDivisionError:
    print("Cannot divide by zero")
