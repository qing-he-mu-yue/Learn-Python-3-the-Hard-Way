# 练习 50：你的第一个网站

from flask import Flask
app = Flask(__name__)

# 有人访问 / 才轮到下面这个函数干活，@app.route 就是这么个绑定。
@app.route('/')
def hello_world():
    greeting = "World"
    # 书里这行漏了 f，浏览器上真会显示 "Hello, {greeting}!"，想出 World 得补个 f。
    return 'Hello, {greeting}!'

if __name__ == "__main__":
    app.run()
