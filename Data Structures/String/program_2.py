#Write a program that will check whether a given String is Palindrome or not.

s = input("Enter the string: ")
rev = s[::-1]
if s == rev:
  print("palindrome")
else:
  print("not palindrome")
