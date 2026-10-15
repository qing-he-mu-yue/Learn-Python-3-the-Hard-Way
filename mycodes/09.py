# 练习 9：打印，打印，打印

# 这节的字符串得一个字符一个字符照抄，少个引号、多个空格，结果就不是书上那样了。

days = "Mon Tue Wed Thu Fri Sat Sun"
# Jan\nFeb 里的 \n 就是"到这儿换一行"，月份才一个占一行。
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print("Here are the days: ", days)
print("Here are the months: ", months)

# 三个引号包住的，中间换几行都行，打出来就是排好的那个样子。
print("""
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
""")
