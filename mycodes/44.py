# 练习 44：继承 vs 组合
# 书上这节拆成 a~e 五个文件，我合到一块儿了，每段标着原来的名字。
# 整节只讲一件事：子类想用父类的东西，有几种用法，各是什么效果。
# 一段一段对下来，到最后 ex44e 你会发现：不继承也行，换个零件装进去反而更松快。

# ex44a.py：子类什么都不写，照样能用父类的方法
class Parent(object):

    def implicit(self):
        print("PARENT implicit()")

class Child(Parent):
    pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()
# 两句打出来一模一样，因为 son 压根没自己的 implicit，只能去爹那儿拿。

# ex44b.py：子类写个同名的，父类的就被盖过去了
class Parent(object):

    def override(self):
        print("PARENT override()")

class Child(Parent):

    def override(self):
        print("CHILD override()")

dad = Parent()
son = Child()

dad.override()
son.override()
# dad 打 PARENT，son 打 CHILD。父类那句在 son 身上压根不会出现，被整个盖掉了。

# ex44c.py：靠 super() 把父类那版也跑一遍，前后各加一句自己的
class Parent(object):

    def altered(self):
        print("PARENT altered()")

class Child(Parent):

    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered()")

dad = Parent()
son = Child()

dad.altered()
son.altered()
# dad 只有一句 PARENT。son 是三句，中间那句是 super() 把父类那版又喊了一遍。

# ex44d.py：三种凑一块儿看
# 前面三段单独看都懂，混在一个类里最容易懵，所以书让你在这儿对一遍：
# 同一个子类里，implicit 是白拿、override 是覆盖、altered 是覆盖再夹一次父类。
class Parent(object):

    def override(self):
        print("PARENT override()")

    def implicit(self):
        print("PARENT implicit()")

    def altered(self):
        print("PARENT altered()")

class Child(Parent):

    def override(self):
        print("CHILD override()")

    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered()")

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()

# ex44e.py：干脆不继承，Child 里揣个 Other 替它干活，这就是组合
# 跟继承的区别一句话：继承是"我是你"，组合是"我有你"。
# 继承改父类会连累所有子类；组合各管各的，想换就换掉那个零件。
# 关键就在 __init__ 里那一行 self.other = Other()，造出来揣身上，用的时候转手给它。
class Other(object):

    def override(self):
        print("OTHER override()")

    def implicit(self):
        print("OTHER implicit()")

    def altered(self):
        print("OTHER altered()")

class Child(object):

    def __init__(self):
        self.other = Other()

    def implicit(self):
        self.other.implicit()

    def override(self):
        print("CHILD override()")

    def altered(self):
        print("CHILD, BEFORE OTHER altered()")
        self.other.altered()
        print("CHILD, AFTER OTHER altered()")

son = Child()

son.implicit()    # 自己不干，转手让 other 干，打的是 OTHER implicit
son.override()    # 这个自己写，没转手，打的是 CHILD override
son.altered()     # 前后自己的，中间夹一句 OTHER 的
