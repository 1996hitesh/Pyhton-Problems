#Write a program to check if a given key already exists in a dictionary

def checkKey(dict, key):

    if key in dict.keys():
        print("Present, ", end =" ")
        print("value =", dict[key])
    else:
        print("Not present")

dict = {0: 100, 1:200, 2:300}

key = int(input("Enter key: "))
checkKey(dict, key)
