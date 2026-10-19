# 练习 18：名字、变量、代码、函数

# *args 是"来多少都先收着"，再自己拆；下面那个直接写 arg1、arg2，明显省事。
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# 上面那版绕了一圈，其实白绕——参数个数早就定死了，直接点名就行。
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# 只收一个，多给一个都不行
def print_one(arg1):
    print(f"arg1: {arg1}")

# 一个都不收，括号留空，调用时也别往里塞东西
def print_none():
    print("I got nothin'.")


print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()
