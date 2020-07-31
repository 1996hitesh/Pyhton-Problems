s = input("Enter file name: ")
try:
    file = open(s)
    content = file.read()
    print(content)
    file.close()
except FileNotFoundError:
    print("file with this name does not exist")
