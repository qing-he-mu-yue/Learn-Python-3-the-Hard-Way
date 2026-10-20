# 练习 24：更多练习

print("Let's practice everything.")
print('You\'d need to know \'bout escapes with \\ that do:')
print('\n newlines and \t tabs.')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("--------------")
print(poem)
print("--------------")


five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)

# 下面两行是同一个意思，两种写法：{} 留空位再 .format() 往里塞，或者 f"" 直接写在句子里。
print("With a starting point of: {}".format(start_point))
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(start_point)
# formula 是个三元组，比如 (5000000.0, 5000.0, 50.0)。
# 前面加个 *，就是把元组拆开，一个一个当参数递进去，正好对上三个 {}。
# 不加 * 会怎样？整个元组被当成一个参数，只填第一个 {}，后面两个直接报"没给够"。
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))
