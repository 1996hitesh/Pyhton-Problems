n = int(input("Enter the value of n: "))
file = open("Test.txt")
for i in range(n):
    content = file.readline()
    print(content,end="")
file.close()
