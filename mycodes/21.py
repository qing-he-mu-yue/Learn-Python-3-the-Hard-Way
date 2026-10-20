# 练习 21：函数可以返回东西

def add(a, b):
    print(f"ADDING {a} + {b}")
    # return 把结果递回去，所以 age = add(30, 5) 跑完，age 就成 35 了。
    return a + b

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} / {b}" )
    return a / b


print("Let's do some math with just functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")


# 附加题，书上说先照抄一遍再自己算，别急着翻答案。
print("Here is a puzzle.")

# 这一长串得从最里面的 divide 算起，一层层往外剥。但说实话，现在 Vibe Coding 这么牛了，抠这些细节的意义何在呢？不太懂啊，但是这种感觉了解了确实很爽
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", what, "Can you do it by hand?")
