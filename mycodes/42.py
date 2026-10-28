# 练习 42：Is-A、Has-A、对象和类

# 这节就干一件事：把 is-a 和 has-a 分清楚。
# is-a 是继承，"我是你的一种"，Dog(Animal) 就是 Dog is-a Animal。
# has-a 是属性，"我身上挂着一个"，self.name = name 就是 Dog has-a name。
# 书里每行都标一遍 (is-a)、(has-a)，标多了反而糊，这里只在关键处点一句。

# 空壳一个，只为让 Dog、Cat 有个共同的爹
class Animal(object):
    pass

# Dog is-a Animal，继承来的；name 是它自己 has-a 的，Animal 那边没有
class Dog(Animal):

    def __init__(self, name):
        self.name = name

# Cat 同理，也是 Animal 的一种
class Cat(Animal):

    def __init__(self, name):
        self.name = name

# Person 不继承谁。pet 先摆个 None，因为这会儿还不知道养啥
class Person(object):

    def __init__(self, name):
        self.name = name
        self.pet = None

# Employee is-a Person。super 那句是"把爹的 __init__ 也跑一遍"，
# 不跑的话 self.name 压根不会被赋值，后面一用就报错
class Employee(Person):

    def __init__(self,name, salary):
        super(Employee, self).__init__(name)
        self.salary = salary

class Fish(object):
    pass

# Salmon 和 Halibut 都是 Fish 的一种，除了名字没别的
class Salmon(Fish):
    pass

class Halibut(Fish):
    pass


# ---- 下面造对象，看 is-a 怎么落到具体东西上 ----

rover = Dog("Rover")
satan = Cat("Satan")
mary = Person("Mary")
mary.pet = satan

frank = Employee("Frank", 120000)
frank.pet = rover
# 这一句能跑通，靠的就是 is-a：frank 是 Employee，Employee 继承 Person，
# Person 身上那个 pet 它才有得挂。

flipper = Fish()
crouse = Salmon()
harry = Halibut()
