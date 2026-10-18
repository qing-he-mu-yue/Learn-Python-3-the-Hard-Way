# 练习 17：更多文件

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# 这两行其实能挤成一行：open(from_file).read()。书上是故意拆开，说白了，目的就是看清"开"和"读"是两件事。
in_file = open(from_file)
indata = in_file.read()

print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

# 复制说白了就是全读出来再原样写过去，exists() 只是先看看目标文件在不在。
out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

out_file.close()
in_file.close()
