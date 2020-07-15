#Write a program to count the number of upper and lower case letters in a String

upper = 0
lower = 0

s = input("enter string: ")
for letter in s:
  if(letter.islower()):
    lower += 1
  elif(letter.isupper()):
    upper += 1

print("Uppercase letters = {}    Lowercase letters = {}".format(upper,lower))
