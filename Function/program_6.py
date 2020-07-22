#Write a function that takes a number as a parameter and checks
#whether the number is prime or not.

def prime(n):
  if(n%2==0):
    return False
  for i in range(3,n//2,2):
    if n%i == 0:
      return False

  return True


n = int(input("Enter number: "))
res = prime(n)
if res == True:
  print("Prime")
else:
  print("Not Prime")
