#Write a program to replace last value of tuples in a list to 100.

given_list = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
final_list = []
for tup in given_list:
  li = list(tup)
  li[2] = 100
  tup = tuple(li)
  final_list.append(tup)

print(final_list)
