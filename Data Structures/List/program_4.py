# Write a program to print the number of occurrences of a specified element in a list.

def countX(lst, x):
    return lst.count(x)

lst = [10,15,2,1,2,3,10,5,9,8,8]     #defining the list
x = int(input("Enter the element to check the occurenece : "))
result = countX(lst,x)
print("Element {} occured in list {} times".format(x,result))
