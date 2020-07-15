#Write a program to sum all the values in a dictionary,
#considering the values will be of int type.

dict1 = {0: 100, 1:200, 2:300}
s = 0
for key in dict1.keys():
  s += dict1[key]

print("sum of all the values: ",s)
