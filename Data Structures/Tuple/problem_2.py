#Write a program to check whether an element exists in a tuple or not.

x = int(input("Enter element to search: "))
t_1 = (1,2,3,4,5,6,7,8,9,10)      #initializing a tuple
if x in t_1:
  print("Element exist")
else:
  print("Element not found")
