# 练习 15：读取文件

from sys import argv

script, filename = argv

# open() 只是把文件"翻开"，想看内容还得再 .read() 一下。这种模式确实好用，比 Java 的好多了
txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
