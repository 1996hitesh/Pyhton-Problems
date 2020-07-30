file = open("Test.txt")
content = file.readlines()
longest = len(content[0])
longest_word = content[0]
for word in content:
    if len(word)>longest:
        longest = len(word)
        longest_word = word
print(longest_word,end="")
file.close()
