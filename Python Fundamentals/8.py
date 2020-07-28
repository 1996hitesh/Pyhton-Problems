x = int(input())
sum = 0
while x!=0:
  r = x%10
  sum += r
  x //= 10
print(sum)
