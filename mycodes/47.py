# 练习 47：自动化测试

class Room(object):

    def __init__(self,name, description):
        self.name = name
        self.description = description
        self.paths = {}

    def go(self, direction):
        return self.paths.get(direction, None)

    def add_paths(self, paths):
        self.paths.update(paths)

# nose 早不维护了，换成 pytest：assert_equal(a, b) 直接写 assert a == b。
# 跑法也是 py -m pytest -v。
# 文件名和函数名都得 test_ 开头，pytest 才会自己去找。
# 名字不对的话，跑起来显示"0 个测试"——那不是报错，是它压根没看见你的测试。
def test_room():
    gold = Room("GoldRoom",
    """This room has gold in it you can grab. There's a
    door to the north.""" )
    assert gold.name == "GoldRoom"
    assert gold.paths == {}

def test_room_paths():
    center = Room("Center", "Test room in the center." )
    north = Room("North", "Test room in the north.")
    south = Room("South", "Test room in the south.")

    center.add_paths({'north': north, 'south': south})
    assert center.go('north') == north
    assert center.go('south') == south

def test_map():
    start = Room("Start", "You can go west and down a hole." )
    west = Room("Trees", "There are trees here, you can go east.")
    down = Room("Dungeon", "It's dark down here, you can go up.")

    start.add_paths({'west': west, 'down': down})
    west.add_paths({'east': start})
    down.add_paths({'up': start})

    assert start.go('west') == west
    assert start.go('west').go('east') == start
    assert start.go('down').go('up') == start
