# 练习 33：While 循环

i = 0
numbers = []

# i 每次加 1，加到 6 这循环就停了；要是忘了写 i = i + 1，可就转个没完了。
while i < 6:
    print(f"At the top i is {i}")
    numbers.append(i)

    i = i + 1
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")


print("The numbers: ")

for num in numbers:
    print(num)
