n = input("Enter the input to append: ")
file = open("Test.txt",'a')
file.write(n)
file.close()
