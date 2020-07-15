#Write a program to iterate over a dictionary using for loop and print the keys
#alone, values alone and both keys and values.

dict = {0: 100, 1:200, 2:300}

print("keys of the dictionary are:")
for key in dict.keys():
  print(key)

print("values of the dictionary are:")
for key in dict.keys():
  print(dict[key])

print("keys and values of the dictionary are:")
for key in dict.keys():
  print("key = {} value = {}".format(key,dict[key]))
