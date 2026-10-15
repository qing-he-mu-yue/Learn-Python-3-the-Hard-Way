# 练习 8：打印，打印

formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
# 把 formatter 自己塞进去，每个 {} 里又冒出 4 个，4×4 就成 16 个了。
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
"Try your",
"Own text here",
"Maybe a poem",
"Or a song about fear"
))
