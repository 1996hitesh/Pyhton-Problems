a = input("Enter number:")
try:
    for i in range(2,int(a)//2):
        if(int(a)==1):
            print("Not a Prime Number")
        elif(int(a)%i==0):
            print("Not a Prime Number")
            break
    else:
        print("Prime Number")
except ValueError:
    print("Please Input only numbers")
