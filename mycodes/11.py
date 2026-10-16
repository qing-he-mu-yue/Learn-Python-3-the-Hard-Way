# 练习 11：提问

print("How old are you?", end=' ')
# 跑到这儿会停住等你回一句，敲的那一整行就进了 age。说白了就跟 cin cout 差不多
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weigh?", end=' ')
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")
