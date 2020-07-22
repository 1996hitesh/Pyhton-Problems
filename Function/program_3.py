#Write a function to calculate and return the factorial of a number
#(a non-negative integer).

def fact(n):
  if n == 1:
    return 1

  f = n*fact(n-1)
  return f

n = int(input("Enter number: "))
res = fact(n)
print(res)
