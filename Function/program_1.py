#Write a function to return the sum of all numbers in a list.

def sumofList(li):
  s = 0
  for ele in li:
    s += ele
  return s

mylist = [8, 2, 3, 0, 7]
res = sumofList(mylist)
print(res)
