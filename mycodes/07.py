# 练习 7：更多打印

print("Mary had a little lamb.")
print("Its fleece was white as {}.".format('snow'))
print("And everywhere that Mary went.")
# "." * 10 就是把点重复十遍，跟连打十个点一个意思。
print("." * 10) # 打出来是 ..........，十个点，不是十个 ".

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# end=' ' 就是"这句别换行，空一格接着往下打"。C++的换行是\n
# 把 end 删了试试，Cheese 和 Burger 会断成两行，拼不成一个词。
print(end1 + end2 + end3 + end4 + end5 + end6, end=' ')
print(end7 + end8 + end9 + end10 + end11 + end12)
