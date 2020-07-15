#Write a program to remove a given item from the set.

my_set = {100,15,21,14,18,32}      #initializing a set
x = int(input("enter the item you want to remove: "))
my_set.remove(x)
print(my_set)
