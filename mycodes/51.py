# 练习 51：从浏览器获取输入

from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/hello")
def index():
    # /hello?name=Frank 里的 name 就从 request.args 拿。
# 页面则是 render_template 去 templates/ 里找的。
    name = request.args.get('name', 'Nobody')

    if name:
        greeting = f"Hello, {name}"
    else:
        greeting = "Hello World"

    return render_template("index.html", greeting=greeting)

if __name__ == "__main__":
    app.run()
