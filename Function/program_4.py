# Write a function that accepts a string and prints the number of
#upper case letters and lower case letters in it.

def upperandlower(s):
  print("Upper case letter: ",end=" ")
  for letter in s:
    if(letter.isupper()):
      print(letter + " ",end = "")
  print()
  print("Lower case letter: ",end=" ")
  for letter in s:
    if(letter.islower()):
      print(letter + " ",end =" ")

s = input("Enter the string: ")
upperandlower(s)
