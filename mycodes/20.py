# 练习 20：函数和文件

from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read())

# 读一遍之后"针"停在文件末尾，seek(0) 把它拨回开头才能重新一行行读，跟倒磁带一个意思。
def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print(line_count, f.readline())

current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
