# 练习 32：循环和列表

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# 第一种 for：挨个把列表里的东西拿出来，一次一个
for number in the_count:
    print(f"This is count {number}")

# 跟上面一模一样，只是换了个列表、换了个变量名
for fruit in fruits:
    print(f"A fruit of type: {fruit}")

# 列表里混着数字和字符串也能这么走，for 不挑。
# 这里必须写 {}，因为 i 里可能是 1 也可能是 'pennies'，写死引号或者数字都会错一半。
for i in change:
    print(f"I got {i}")

# 先建个空列表，待会儿往里塞
elements = []

# range(0, 6) 是 0 到 5，右边那个 6 不算；append 是列表自带的方法，往末尾塞一个。
for i in range(0, 6):
    print(f"Adding {i} to the list.")
    elements.append(i)

# 塞完了再走一遍打出来
for i in elements:
    print(f"Element was: {i}")
