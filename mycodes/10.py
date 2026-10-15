# 练习 10：那是什么？（转义序列）

# \t 空一格，\n 换一行；真想打出 \ 得写两个 \\，写一个会被当成转义的开头。
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)
