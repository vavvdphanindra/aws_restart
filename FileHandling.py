"""
file = open("FileExample.txt","w")
file.write("Hello World")
file.close()


file = open("FileExample.txt","r")
contents = file.read()
print(contents)
file.close()
"""

file = open("FileExample.txt","a")
file.write("\nThis is Phanindra")
file.close()