#Write a program to accept a welcome message through command
#line arguments and display the file name along with the welcome message

from sys import argv

file_name = argv[0]
wel_mes = argv[1]

print("File Name: {}  Welcome Message: {}".format(file_name,wel_mes))
