# 练习 38：对列表做操作

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee",
"Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1]) # -1 是"倒数第一个"，不用管列表多长
print(stuff.pop())
print(' '.join(stuff)) # 用空格把列表粘成一长串
# [3:5] 切出第 4、5 两个，第 6 个不要；join 再用 # 把它俩粘回去。
print('#'.join(stuff[3:5])) # 先切后粘：切出两个，再用 # 连起来
