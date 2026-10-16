# 练习 13：参数、解包、变量

from sys import argv
# 这行得带着参数在命令行里跑，双击是跑不起来的。
# 跑 py 13.py a b c：a、b、c 依次落到 first、second、third，脚本名自己占 script。少传一个就报错。
script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
