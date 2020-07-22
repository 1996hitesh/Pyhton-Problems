#Write a function to print the even numbers from a given list.
#List is passed to the function as an argument.

def evenprint(li):
  evenlist = []
  for ele in li:
    if ele%2 == 0:
      evenlist.append(ele)
  print("Even elements: ",evenlist)

li = [1, 2, 3, 4, 5, 6, 7, 8, 9]      #Sample List
evenprint(li)
