#Write a function to return the reverse of a string.

def revrese_string(s):
  rev = s[::-1]
  return rev

s = input("Enter string: ")
res = revrese_string(s)
print(res)
