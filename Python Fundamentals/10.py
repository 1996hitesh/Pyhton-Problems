x = int(input())
y = 0
temp = x
while x>0:
  r = x%10
  y = 10*y + r
  x //= 10
if temp == y:
  print("Palindrome")
else:
  print("Not Palindrome")
