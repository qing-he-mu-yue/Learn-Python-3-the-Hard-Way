# 练习 5：更多变量和打印

my_name = 'Zed A. Shaw'
my_age = 35 # 岁
my_height = 74 # 英寸，不是厘米
my_weight = 180 # 磅，一磅差不多九两
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

# 引号前加个 f，{} 里写名字就行，{my_age} 直接变成 35。说白了，和C++的字符串拼接差不多嘛
print(f"Let's talk about {my_name}.")
print(f"He's {my_height} inches tall.")
print(f"He's {my_weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")

# 这行是这节唯一要动脑的：三个数加一起，{} 的次序得跟后面变量对得上；错一个位置，数就串了。
total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height}, and {my_weight} I get {total}.")
