s = input("Enter Word:")
count = 0
file = open("Test.txt")
content = file.readlines()
for word in content:
    if s in word:
        count += 1
print("Word Count = ",count)
file.close()
