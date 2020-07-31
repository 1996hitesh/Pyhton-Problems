li = [2,5,10,0,-7,6,-9,1,-4,-3]
n = int(input("Enter the index: "))
try:
    if li[n]>0:
        print("Positive Number")
    elif li[n]<0:
        print("Negative Number")
    else:
        print("Zero")
except IndexError:
    print("Enter index between 0 to 9")
