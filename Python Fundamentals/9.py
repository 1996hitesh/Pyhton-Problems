x = int(input())
y = 0
while x>0:
  r = x%10
  y = 10*y + r
  x //= 10
print(y)
