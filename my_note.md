# ch3 实践记录

**基于 Python 的 Web 框架有 Django, Flask, Tornado 等，Flask 属于轻量级框架。**

> 参考资料：[what is a web Framework? -Jeff Knupp](https://jeffknupp.com/blog/2014/03/03/what-is-a-web-framework/)

## 安装体验 flask 框架

> 查阅官方文档：[http://flask.pocoo.org](http://flask.pocoo.org)

`pip install flask`  // 基于 python2.x

`pip3 install flask`  //基于 python3.x

创建 hello.py , 写入以下：

```
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
  return "Hello World!"

if __name__ == "__main__":
  app.run()
```

运行 hello.py, 得到：

```
$ python3 hello.py
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```
在浏览器访问 http://127.0.0.1:5000 ，看到如下图：

![Selection_011](https://i.loli.net/2017/09/02/59aa350de3ba7.png)

## 体验 render_template 网页模板

> 参考资料：[flask 的 render_template 官方资料示例](http://flask.pocoo.org/docs/0.12/quickstart/#rendering-templates)

开始时，没有将 hello.html 文本放在 templates 文件夹中，访问 `/hello/` 和 `/hello/allen` 总是返回 server error 错误。

查看官方示例：

> Flask will look for templates in the templates folder. So if your application is a module, this folder is next to that module, if it’s a package it’s actually inside your package:

**case 1: a module**
```
/application.py
/templates
   /hello.html
```
**case 2: a package**
```
/application
  /__init__.py
  /templates
    /hello.html
```
### 感受

`weatherApp.py` 其实是对 `ch2.py` 后面执行返回的另一种形式展现。所以前面从 API request 结果 和 保存为 dict 类型数据可以保持不变。

## jinj2 模板继承

> 参考资料：[template inheritance](http://jinja.pocoo.org/docs/2.9/templates/#template-inheritance)

```
{% extend "index.html" %}
{% block content %}
```
