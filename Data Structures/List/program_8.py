#Write a program to remove the first occurrence of a specified element from a list.

def RemoveIthWord(list, word):
    for i in range(0, len(list)):
        if (list[i] == word):
            del(list[i])
            return True

    return False

# Defining the list
list = [1,2,3,1,2,4,1,5,6]
n = int(input("Enter the element: "))

flag = RemoveIthWord(list, n)

if (flag == True):
    print("Updated list is: ", list)
else:
    print("Item not Updated") 
