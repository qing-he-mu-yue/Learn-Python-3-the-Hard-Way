# 练习 39：字典，哦可爱的字典

# 建一本字典：州名当钥匙，缩写当值
states = {
'Oregon': 'OR',
'Florida': 'FL',
'California': 'CA',
'New York': 'NY',
'Michigan': 'MI'
}

# 再建一本：缩写当钥匙，城市当值
cities = {
'CA': 'San Francisco',
'MI': 'Detroit',
'FL': 'Jacksonville'
}

# 字典随时能加，给个新钥匙赋个值就行
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# 拿钥匙取值，钥匙不存在会直接报 KeyError
print('-' * 10)
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])

# 换一本字典，同一套动作
print('-' * 10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

# 两本连着查：先拿 "Michigan" 查到 "MI"，再拿 "MI" 去查城市
print('-' * 10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

# items() 一次给一对 (钥匙, 值)，for 里两个变量正好接住
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

# 再来一遍，这回走 cities
print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

# 一边走 states，一边拿缩写去 cities 里查，两本一起用
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

print('-' * 10)
# 字典里没有 Texas，用 get 不会报错，顶多给个 None；给个默认值就返回默认值。
state = states.get('Texas')

if not state:
    print("Sorry, no Texas.")

# 第二个参数是默认值：查不到就把这个还给你
city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is: {city}")
