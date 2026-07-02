# flask开发--刘深



# 一、开发环境配置
# 计算机用户的名称
# whoami
# mkdir watchlist
# cd watchlist
# 安装python配置环境略
# python --version
# 安装 Git for
# Windows 后（下一节）附带的 Git Bash
# git --version
# 为了让 Git 知道你是谁，以便在提交代码到版本仓库的时候进行记

# 使用下面的命令设置你的信息：
# git config --global user.name "Grey Li" # 替换成你的名字
# git config --global user.email "withlihui@gmail.com"# 替换成你的邮箱地址
# 现在为我们的项目文件夹创建一个 Git 仓库，这会在我们的项目根
# 目录创建一个 .git 文件夹：
# git init
# # Initialized empty Git repository in ~/watchlist/.git/

# Git 默认会追踪项目文件夹（或者说代码仓库）里所有文件的变化，
# 但是有些无关紧要的文件不需要记录变化，我们在项目根目录创建
# 一个 .gitignore 文件，在文件中写入忽略文件的规则。因为文件内
# 容比较简单 右键使用文本文档编辑
# 编辑界面写入常见的可忽略文件规则：
# *.pyc
# *~
# __pycache__
# .DS_Store

# 将程序托管到 GitHub（可选）
# 这一步是可选的，将程序托管到 GitHub、GitLab 或是 BitBucket 等
# 平台上，可以更方便的备份、协作和部署。这些托管平台作为 Git
# 服务器，你可以为本地仓库创建远程仓库。
# 首先要注册一个 GitHub 账户，点击访问注册页面，根据指示完成
# 注册流程。登录备用。
# 设置 SSH 密钥
# 要在git bash中进行
# $ cat ~/.ssh/id_rsa.pub
# 如果显示“No such file or directory”，就使用下面的命令生成 SSH
# 密钥对，否则复制输出的值备用：
# $ ssh-keygen
# 一路按下 Enter 采用默认值，最后会在用户根目录创建一个 .ssh 文
# 件夹，其中包含两个文件，id_rsa 和 id_rsa.pub，前者是私钥，不
# 能泄露出去，后者是公钥，用于认证身份，就是我们要保存到
# GitHub 上的密钥值。再次使用前面提到的命令获得文件内容：
# $ cat ~/.ssh/id_rsa.pub

# 选中并复制输出的内容，访问 GitHub 的 SSH 设置页面（导航栏头
# 像 - Settings - SSH and GPG keys），点击 New SSH key 按钮，
# 将复制的内容粘贴到 Key 输入框里，再填一个标题，比如“My
# PC”，最后点击“Add SSH key”按钮保存。


# 创建远程仓库
# 访问新建仓库页面（导航栏“+” - New repository），在“Repository
# name”处填写仓库名称，这里填“watchlist”即可，接着选择仓库类型
# （公开或私有）等选项，最后点击“Create repository”按钮创建仓
# 库。
# 因为我们已经提前创建了本地仓库，所以需要指定仓库的远程仓库
# 地址（如果还没有创建，则可以直接将远程仓库克隆到本地）：
# $ git remote add origin git@github.com:greyli/
# watchlist.git # 注意更换地址中的用户名
# 这会为本地仓库关联一个名为“origin”的远程仓库，注意将仓库地址
# 中的“greyli”换成你的 GitHub 用户名

# 创建虚拟环境
# 虚拟环境是独立于 Python 全局环境的 Python 解释器环境，使用它
# 的好处如下：
# • 保持全局环境的干净
# • 指定不同的依赖版本
# • 方便记录和管理依赖



# 我们首先使用 pip 安装 Pipenv，Windows 系统使用下面的命令：
# $ pip install pipenv

# 创建虚拟环境后，我们可以使用 pipenv shell 命令来激活虚拟环
# 境，如下所示（执行 exit 可以退出虚拟环境）：
# $ pipenv shell


# 如果你不想每
# 次都激活虚拟环境，可以在命令前添加 pipenv run 前缀，比如
# pipenv run pip list 即表示在虚拟环境内执行 pip list 命令。


# 安装 Flask
# 无论是否已经激活虚拟环境，你都可以使用下面的命令来安装
# Flask：
# $ pipenv install flask
# 这会把 Flask 以及相关的一些依赖包安装到对应的虚拟环境，同时
# Pipenv 会自动更新依赖文件。
# 提示 如果你没有使用虚拟环境，记得将 Flask 更新到最新版本
# （pip install -U flask）。

# 小结
# 使用 git status 命令可以查看当前仓库的文件变动状
# 态：
# $ git status

# 下面让我们将文件改动提交进 Git 仓库，并推送到在 GitHub 上创建
# 的远程仓库：
# $ git add .
# $ git commit -m "I'm ready!"
# $ git push -u origin master # 如果你没有把仓库托管到
# GitHub，则跳过这条命令，后面章节亦同

# 这里最后一行命令添加了 -u 参数，会将推送的目标仓库和分支设为
# 默认值，后续的推送直接使用 git push 命令即可。在 GitHub 上，
# 你可以通过 https://github.com/你的用户名/watchlist 查看你的仓库
# 内容



# 二、FLASK开发
# Hello, Flask!
# 追溯到最初，Flask 诞生于 Armin Ronacher 在 2010 年愚人节开的
# 一个玩笑。后来，它逐渐发展成为一个成熟的 Python Web 框架，
# 越来越受到开发者的喜爱。目前它在 GitHub 上是 Star 数量最多的
# Python Web 框架，没有之一。
# Flask 是典型的微框架，作为 Web 框架来说，它仅保留了核心功
# 能：请求响应处理和模板渲染。这两类功能分别由
# Werkzeug（WSGI 工具库）完成和 Jinja（模板渲染库）完成，因
# 为 Flask 包装了这两个依赖，我们暂时不用深入了解它们。
# from flask import Flask
# from flask import url_for

from flask import Flask, url_for
app = Flask(__name__)
# @app.route('/')
# @app.route('/home')
# @app.route('/')
# @app.route('/index')
# @app.route('/home')
# def hello():
    # return 'Welcome to My Watchlist!'
    # return '<h1>Hello Totoro!</h1><img src="http://helloflask.com/totoro.gif">'
# @app.route('/user/<name>')
# def user_page(name):
    # # return 'User page'+" "+name
      # return 'User: %s' % name
@app.route('/')
def hello():
    return 'Hello'
@app.route('/user/<name>')
def user_page(name):
    return 'User: %s' % name
@app.route('/test')
def test_url_for():
    # 下面是一些调用示例（请在命令行窗口查看输出的 URL）：
    print(url_for('hello')) # 输出：/
    # 注意下面两个调用是如何生成包含 URL 变量的 URL 的
    print(url_for('user_page', name='greyli')) 
    # 输出：/user/greyli
    print(url_for('user_page', name='peter')) 
    # 输出：/ user/peter
    print(url_for('test_url_for')) 
    # 输出：/test
    # # 下面这个调用传入了多余的关键字参数，它们会被作为查询字
    # 符串附加到 URL 后面。
    print(url_for('test_url_for', num=2)) 
    # 输出：/test?num=2
    return 'Test page'

if __name__ == '__main__':
    # host="0.0.0.0" 开放局域网访问，port=8080自定义端口
    app.run(host="0.0.0.0", port=8080, debug=True)



# 一、__name__ 是什么（必懂）
# __name__ 是 Python 内置特殊变量，双下划线包裹，俗称 “魔法变量”。
# 程序运行时分两种情况：
# 直接运行这个文件（python app.py）
# 此时 __name__ 的值 = 字符串 "__main__"
# 别的文件 import 导入这个脚本
# 此时 __name__ 的值 = 当前文件名（不带 .py），比如文件叫 app.py，值就是 "app"
# 二、Flask(__name__) 为什么要传它？是固定写法吗？
# 1. 属于 Flask 标准固定写法，几乎所有项目都这么写
# 2. 传给 Flask 的作用
# Flask 需要靠这个参数定位项目根目录，自动查找：
# 静态文件夹 static/（css、js、图片）
# 模板文件夹 templates/（html 页面）
# 项目内资源文件、相对路径
# 举个对比
# app = Flask(__name__) → 自动以当前文件所在文件夹为项目根目录（最省心）
# 如果你乱写 app = Flask("abc") 也能跑简单接口，但读取静态文件、模板时会路径报错。
# 三、配套的 if __name__ == '__main__': 一起讲
# python
# 运行
# if __name__ == '__main__':
    # app.run(host="0.0.0.0", port=8080, debug=True)
# 逻辑：
# 只有直接执行本文件时，才启动服务；
# 如果别人导入你的 app.py 当作模块，不会自动运行服务，避免端口冲突、重复启动。
# 四、总结
# __name__ 是 Python 自带变量，不是 Flask 专属；
# Flask(__name__) 是行业标准固定写法，不要随便替换；
# 作用：给框架标记项目路径，加载静态资源、模板；
# if __name__ == "__main__" 配套使用，控制服务只在直接运行脚本时启动。


# @app 是装饰器语法，用来把下面的函数绑定成网页路由接口；@ 是 Python 装饰器标记，app 就是你前面创建的 Flask 实例对象 app = Flask(__name__)。
# 1. 拆开两段理解
# ① @ 符号
# Python 专用语法糖，代表「装饰器」，作用：给下面的函数附加额外功能，不改动函数本身代码。
# ② app.route('/')
# app = 你的 Flask 程序实例
# route() 是 app 自带的方法，功能：注册 URL 地址，告诉 Flask：访问哪个网址，执行哪个函数。
# 合起来 @app.route('/') 完整含义：
# 把下方的 hello() 函数装饰成根路径 / 的接口，浏览器访问 http://127.0.0.1:5000/ 就自动执行 hello 函数，返回内容给页面。
# 2. 完整流程对照你的代码
# python
# 运行
# from flask import Flask
# 创建程序实例，变量名叫app
# app = Flask(__name__)

# 装饰器：绑定URL / 和下面的hello函数
# @app.route('/')
# def hello():
    # return 'Welcome to My Watchlist!'
# 执行逻辑：
# app.route('/') 生成一个路由规则
# @ 把规则挂载到 hello 函数上
# 网站收到访问 / 的请求 → 自动运行 hello ()
# 3. 举多个路由例子更好懂
# python
# 运行
# 访问首页 /
# @app.route('/')
# def index():
    # return "首页"

# 访问 /about
# @app.route('/about')
# def about():
    # return "关于我们"

# 访问 /user/123
# @app.route('/user/<id>')
# def user(id):
    # return f"用户编号：{id}"
# 每一行 @app.route(地址) 都是靠 app 这个实例来注册路由。
# 4. 关键小结
# app 不是关键字，是你自己定义的变量，你改名也能用：
# python
# 运行
# 换成别的变量名，对应装饰器也要同步改
# web = Flask(__name__)
# @web.route('/')
# def hello():
    # return "测试"
# @app.route() 是 Flask 固定搭配写法，所有页面接口都要靠它声明；
# 装饰器本质简化了复杂的函数注册逻辑，不用写 hello = app.route('/')(hello) 这种底层代码。


    
# 日常最常用两种，分场景
# 1、本地开发首选：python app.py（90% 人日常用）
# 优点
# 不用每次敲环境变量，打开终端直接运行
# 写法简单，不会出现你刚才 flask run app.py 参数报错
# 端口、调试、跨机访问直接写在代码里，不用输命令参数
# 使用条件
# 文件末尾必须加这段代码：
# python
# 运行
# if __name__ == '__main__':
    # debug=True 自动刷新代码
    # app.run(debug=True, host="0.0.0.0", port=5000)
# 启动命令只需要：
# bash
# 运行
# python app.py
# 2、官方标准方式：set FLASK_APP=app.py + flask run（官方推荐，适合线上 / 规范项目）
# 适用场景
# 规范项目、部署上线、多文件拆分的 Flask 项目
# 使用蓝图、工厂模式创建 app 的大型项目
# Windows 完整命令
# bash
# 运行
# set FLASK_APP=app.py
# set FLASK_ENV=development
# flask run
# 简单总结
# 自己写小 demo、测试、日常调试：优先 python app.py
# 正规项目、打包部署、团队协作：用 flask run 环境变量方式




# 一、直接改代码（最常用，推荐）
# 修改 app.run() 里的 host 和 port 参数：
# python
# 运行
# from flask import Flask
# app = Flask(__name__)

# @app.route('/')
# def hello():
    # return 'Welcome to My Watchlist!'

# if __name__ == '__main__':
    # # host="0.0.0.0" 允许局域网其他设备访问
    # # port=8080 自定义端口，默认是5000
    # app.run(host="0.0.0.0", port=8080, debug=True)

# 参数说明
# host="127.0.0.1"（默认）：只能自己本机浏览器打开，别人电脑访问不了
# host="0.0.0.0"：开放所有 IP，同 WiFi 下手机 / 其他电脑都能访问你的项目
# port=xxxx：自定义端口，不要和其他程序冲突（如 80、3306、6379）
# 启动直接运行：
# bash
# 运行
# python app.py

# 访问地址示例：http://192.168.1.100:8080（你的本机局域网 IP）
# 二、不用改代码，命令行指定（flask run 方式）
# 终端设置环境变量并启动
# cmd
# set FLASK_APP=app.py
# set FLASK_ENV=development
# --host 指定IP  --port 指定端口
# flask run --host=0.0.0.0 --port=8080

# 优势：临时换端口不用修改源码，适合临时测试。
# 补充小提示
# 端口小于 1024（如 80）Windows 需要管理员终端运行；
# debug=True 仅开发用，正式上线必须删掉；
# 查看本机局域网 IP：cmd 输入 ipconfig，找到无线局域网适配器 IPv4 地址。


# 分两种使用人群，主流选择很清晰
# 1. 个人写 Demo、本地调试、自学（90% 普通人最常用）
# 直接写在代码 app.run(host,port) 里
# 就是你现在这种写法：
# python
# 运行
# app.run(host="0.0.0.0", port=8080, debug=True)

# 优点
# 一劳永逸，每次 python app.py 自动生效，不用输长命令
# 不用记 flask run 一堆参数，新手不会报参数错误
# 代码打开就能看到配置，换电脑、重启环境都不用重新设置
# 适合你当前场景
# 你是自己本地练习、单机开发，优先用这种。
# 2. 正规项目、团队协作、临时切换端口、线上部署（企业 / 老手用）
# flask run --host=0.0.0.0 --port=xxxx 命令行传参
# 优点
# 不改源码，多人共用一份代码不会互相冲突端口
# 临时测试不同端口只改命令，不用来回修改保存代码
# 符合 Flask 官方标准启动规范，上线容器、服务器部署通用
# 缺点
# 每次新开终端都要完整输入一长串指令，麻烦。
# 一句话总结
# 自学、自己玩、小脚本：代码内写死 host 和 port（最常用）
# 工作项目、多人开发、频繁换端口测试：命令行传参启动


# 修改后浏览器访问地址
 # * Running on http://127.0.0.1:8080
 # * Running on http://192.168.1.111:8080



# 解剖时间
# 下面我们来分解这个 Flask 程序，了解它的基本构成。
# 首先我们从 flask 包导入 Flask 类，通过实例化这个类，创建一个
# 程序对象 app：
# from flask import Flask
# app = Flask(__name__)
# 接下来，我们要注册一个处理函数，这个函数是处理某个请求的处
# 理函数，Flask 官方把它叫做视图函数（view funciton），你可以理
# 解为“请求处理函数”。
# 所谓的“注册”，就是给这个函数戴上一个装饰器帽子。我们使用
# app.route() 装饰器来为这个函数绑定对应的 URL，当用户在浏览
# 器访问这个 URL 的时候，就会触发这个函数，获取返回值，并把返
# 回值显示到浏览器窗口：
# @app.route('/')
# def hello():
# return 'Welcome to My Watchlist!'
# 填入 app.route() 装饰器的第一个参数是 URL 规则字符串，这里的
# /指的是根地址。
# 我们只需要写出相对地址，主机地址、端口号等都不需要写出。所
# 以说，这里的 / 对应的是主机名后面的路径部分，完整 URL 就是
# http://localhost:5000/。如果我们这里定义的 URL 规则是 /hello，
# 那么完整 URL 就是 http://localhost:5000/hello 。
# 整个请求的处理过程如下所示：
# 1. 当用户在浏览器地址栏访问这个地址，在这里即 http://
# localhost:5000/
# 2. 服务器解析请求，发现请求 URL 匹配的 URL 规则是 /，因此
# 调用对应的处理函数 hello()
# 3. 获取 hello() 函数的返回值，处理后返回给客户端（浏览器）
# 4. 浏览器接受响应，将其显示在窗口上
# 提示 在 Web 程序的语境下，虽然客户端可能有多种类型，但在本
# 书里通常是指浏览器。

# 程序发现机制
# 如果你把上面的程序保存成其他的名字，比如 hello.py，接着执行
# flask run 命令会返回一个错误提示。这是因为 Flask 默认会假设
# 你把程序存储在名为 app.py 或 wsgi.py 的文件中。如果你使用了其
# 他名称，就要设置系统环境变量 FLASK_APP 来告诉 Flask 你要启动
# 哪个程序。
# Flask 通过读取这个文件对应的模块寻找要运行的程序实例，你可
# 以把它设置成下面这些值：
# • 模块名
# • Python 导入路径
# • 文件目录路径


# 一、核心问题说明
# 当文件不叫 app.py / wsgi.py（比如 hello.py），直接敲 flask run 会报错，因为 Flask 命令行工具默认只自动识别这两个文件名，找不到 app 实例就启动失败。
# 两种解决方式：设置 FLASK_APP 环境变量、直接用 python 脚本运行。
# 方式 1：python hello.py 运行（最简单，不用配环境变量）
# 脚本末尾必须加启动代码：
# python
# 运行
# from flask import Flask
# app = Flask(__name__)

# @app.route('/')
# def index():
    # return "Hello Flask"

# 本地直接运行入口
# if __name__ == '__main__':
    # app.run(debug=True)
# 执行命令：
# bash
# 运行
# python hello.py
# 原理：不走 flask 命令行工具，直接把脚本当作 Python 文件执行，不受文件名限制。
# 方式 2：使用 flask run 命令（需要配置 FLASK_APP）
# Windows CMD 终端
# cmd
# set FLASK_APP=hello
# flask run
# Windows PowerShell
# powershell
# $env:FLASK_APP="hello"
# flask run
# Mac / Linux
# bash
# 运行
# export FLASK_APP=hello
# flask run
# 补充说明
# FLASK_APP=hello 代表导入 hello.py 模块，自动寻找模块内名为 app 的 Flask 实例；
# 如果实例变量不叫 app，比如 myapp = Flask(__name__)，写法：
# cmd
# set FLASK_APP=hello:myapp
# flask run
# 开启调试模式（自动重启）额外配置：
# cmd
# set FLASK_ENV=development
# 二、FLASK_APP 支持的三种赋值格式
# 模块名（最常用）
# 文件 hello.py → FLASK_APP=hello
# 导入路径（指定实例）
# FLASK_APP=hello:app 等价于上面默认写法；自定义实例 hello:myapp
# 文件绝对 / 相对路径
# cmd
# set FLASK_APP=D:\flask\hello.py
# flask run
# 三、两种启动方式对比
# 表格
# 启动方式	优点	缺点
# python hello.py	无需配置环境变量，新手友好	部分 flask 命令行扩展功能无法使用
# flask run	统一标准命令，支持更多参数（host/port）	文件名非 app.py 必须配置 FLASK_APP
# 四、常用拓展启动参数（flask run）
# 指定端口、允许外部访问：
# cmd
# set FLASK_APP=hello
# flask run --host=0.0.0.0 --port=8080





# 管理环境变量
# 现在在启动 Flask 程序的时候，我们通常要和两个环境变量打交
# 道：FLASK_APP 和 FLASK_ENV。因为我们的程序现在的名字是
# app.py，暂时不需要设置 FLASK_APP；FLASK_ENV 用来设置程序运行
# 的环境，默认为 production。在开发时，我们需要开启调试模式
# （debug mode）。调试模式可以通过将系统环境变量 FLASK_ENV 设
# 为 development 来开启。调试模式开启后，当程序出错，浏览器页
# 面上会显示错误信息；代码出现变动后，程序会自动重载。
# 为了不用每次打开新的终端会话都要设置环境变量，我们安装用来
# 管理系统环境变量的 python-dotenv：
# $ pipenv install python-dotenv
# 当 python-dotenv 安装后，Flask 会从项目根目录的 .flaskenv 和
# .env 文件读取环境变量并设置。我们分别使用文本编辑器创建这两
# 个文件，或是使用更方便的 touch 命令创建：
# $ touch .env .flaskenv
# .flaskenv 用来存储 Flask 命令行系统相关的公开环境变量；而 .env
# 则用来存储敏感数据，不应该提交进Git仓库，我们把 .env 添加到
# .gitignore 文件的结尾（新建一行）来让 Git 忽略它。你可以使用编
# 辑器执行这个操作：
# .env
# 在新创建的 .flaskenv 文件里，我们写入一行
# FLASK_ENV=development ，将环境变量 FLASK_ENV 的值设为
# development，以便开启调试模式：
# FLASK_ENV=development
# 实验时间
# 在这个小节，我们可以通过做一些实验，来扩展和加深对本节内容
# 的理解。
# 修改视图函数返回值
# 首先，你可以自由修改视图函数的返回值，比如：
# @app.route('/')
# def hello():
# return u'欢迎来到我的 Watchlist！'
# 返回值作为响应的主体，默认会被浏览器作为 HTML 格式解析，所
# 以我们可以添加一个 HTML 元素标记：
# @app.route('/')
# def hello():
# return '<h1>Hello Totoro!</h1><img src="http://
# helloflask.com/totoro.gif">'
# 保存修改后，只需要在浏览器里刷新页面，你就会看到页面上的内
# 容也会随之变化。


# 修改 URL 规则
# 另外，你也可以自由修改传入 app.route 装饰器里的 URL 规则字符
# 串，但要注意以斜线 / 作为开头。比如：
# @app.route('/home')
# def hello():
# return 'Welcome to My Watchlist!'
# 保存修改，这时刷新浏览器，则会看到一个 404 错误提示，提示页
# 面未找到（Page Not Found）。这是因为视图函数的 URL 改成了
# /home，而我们刷新后访问的地址仍然是旧的 /。如果我们把访问地
# 址改成 http://localhost:5000/home，就会正确看到返回值。
# 一个视图函数也可以绑定多个 URL，这通过附加多个装饰器实现，
# 比如：
# @app.route('/')
# @app.route('/index')
# @app.route('/home')
# def hello():
# return 'Welcome to My Watchlist!'
# 现在无论是访问 http://localhost:5000/、http://localhost:5000/home
# 还是 http://localhost:5000/index 都可以看到返回值。
# 在前面，我们之所以把传入 app.route 装饰器的参数称为 URL 规
# 则，是因为我们也可以在 URL 里定义变量部分。比如下面这个视图
# 函数会处理所有类似 /user/<name> 的请求：
# @app.route('/user/<name>')
# def user_page(name):
# return 'User page'
# 不论你访问 http://localhost:5000/user/greyli，还是 http://
# localhost:5000/user/peter，抑或是 http://localhost:5000/user/甲，
# 都会触发这个函数。通过下面的方式，我们也可以在视图函数里获
# 取到这个变量值：
# @app.route('/user/<name>')
# def user_page(name):
# return 'User: %s' % name
# 修改视图函数名？
# 最后一个可以修改的部分就是视图函数的名称了。首先，视图函数
# 的名字是自由定义的，和 URL 规则无关。和定义其他函数或变量一
# 样，只需要让它表达出所要处理页面的含义即可。
# 除此之外，它还有一个重要的作用：作为代表某个路由的端点
# （endpoint），同时用来生成 URL。对于程序内的 URL，为了避免
# 手写，Flask 提供了一个 url_for 函数来生成 URL，它接受的第一
# 个参数就是端点值，默认为视图函数的名称：
# from flask import url_for
# # ...
# @app.route('/')
# def hello():
# return 'Hello'
# @app.route('/user/<name>')
# def user_page(name):
# return 'User: %s' % name
# @app.route('/test')
# def test_url_for():
# # 下面是一些调用示例（请在命令行窗口查看输出的 URL）：
# print(url_for('hello')) # 输出：/
# # 注意下面两个调用是如何生成包含 URL 变量的 URL 的
# print(url_for('user_page', name='greyli')) # 输
# 出：/user/greyli
# print(url_for('user_page', name='peter')) # 输出：/
# user/peter
# print(url_for('test_url_for')) # 输出：/test
# # 下面这个调用传入了多余的关键字参数，它们会被作为查询字
# 符串附加到 URL 后面。
# print(url_for('test_url_for', num=2)) # 输出：/
# test?num=2
# return 'Test page'
# 实验过程中编写的代码可以删掉，也可以保留，但记得为根地址返
# 回一行问候，这可是我们这一章的任务。
# 本章小结
# 这一章我们为程序编写了主页，同时学习了 Flask 视图函数的基本
# 编写方式。结束前，让我们提交代码：
# $ git add .
# $ git commit -m "Add minimal home page"
# $ git push
# 为了保持简单，我们统一在章节最后一次提交所有改动。在现实世
# 界里，通常会根据需要分为多个 commit；同样的，这里使用 -m 参
# 数给出简单的提交信息。在现实世界里，你可能需要撰写更完整的
# 提交信息。
# 提示 你可以在 GitHub 上查看本书示例程序的对应 commit：
# eca06dc。
# 进阶提示
# • 如果你使用 Python 2.7，为了使程序正常工作，需要在脚本首
# 行添加编码声明 # -*- coding: utf-8-*- ，并在包含中文的
# 字符串前面添加 u 前缀。本书中对于包含中文的字符串均添加
# 了 u 前缀，这在 Python 3 中并不需要。
# • 对于 URL 变量，Flask 还支持在 URL 规则字符串里对变量设
# 置处理器，对变量进行预处理。比如 /user/<int:number> 会
# 将 URL 中的 number 部分处理成整型，同时这个变量值接收
# 传入数字。
# • 因为 Flask 的上下文机制，有一些变量和函数（比如
# url_for函数）只能在特定的情况下才能正确执行，比如视图
# 函数内。我们先暂时不用纠结，后面再慢慢了解。
# • 名字以 . 开头的文件默认会被隐藏，执行 ls 命令时会看不到
# 它们，这时你可以使用 ls -f 命令来列出所有文件。
# • 了解 HTTP 基本知识将会有助于你了解 Flask 的工作原理。



# url_for 带额外参数（查询参数）真实业务场景举例
# url_for(视图函数名, 路由变量=值, 额外键值对) 中，不在路由 <变量> 里的参数，会自动拼接成 ?key=value 查询字符串，也就是你代码里 num=2 的效果 /test?num=2。
# 下面给 5 个企业真实开发高频场景，全部是项目里常用写法。
# 场景 1：分页跳转（最常用）
# 后台列表分页，页面切换时传递页码、每页条数
# python
# 运行
# from flask import Flask, url_for, render_template_string

# app = Flask(__name__)

# @app.route('/article/list')
# def article_list():
    # page = 1
    # page_size = 10
    # # 生成分页跳转链接：/article/list?page=2&page_size=10
    # next_page_url = url_for("article_list", page=page+1, page_size=page_size)
    # # 传给模板渲染分页按钮
    # html = f"""
    # <a href="{next_page_url}">下一页</a>
    # """
    # return html

# if __name__ == '__main__':
    # app.run(debug=True)
# 访问 /article/list，打印 next_page_url 结果：
# /article/list?page=2&page_size=10
# 场景 2：搜索筛选，携带查询条件
# 商品 / 用户搜索，保留关键词、筛选条件跳转页面
# python
# 运行
# @app.route('/goods')
# def goods():
    # keyword = "手机"
    # price_min = 1000
    # # 拼接筛选链接 /goods?keyword=手机&price_min=1000&sort=sale
    # sort_sale = url_for("goods", keyword=keyword, price_min=price_min, sort="sale")
    # sort_price = url_for("goods", keyword=keyword, price_min=price_min, sort="price")
    # return f'''
    # 销量排序：<a href="{sort_sale}">销量优先</a>
    # 价格排序：<a href="{sort_price}">价格优先</a>
    # '''
# 场景 3：列表跳转详情，附带来源页标识
# 从列表点进详情，记录「来源页面 + 页码」，方便详情页返回时回到原列表
# python
# 运行
# @app.route('/user/<uid>')
# def user_detail(uid):
    # # 获取跳转时带的来源参数
    # from flask import request
    # source_page = request.args.get("source_page", "user_list")
    # page = request.args.get("page", 1)
    # # 返回按钮链接，带回原来的页码
    # back_url = url_for(source_page, page=page)
    # return f'用户{uid}详情 <a href="{back_url}">返回列表</a>'

# @app.route('/user/list')
# def user_list():
    # page = 3
    # # 跳转用户详情，额外携带来源标识
    # detail_url = url_for("user_detail", uid=1001, source_page="user_list", page=page)
    # return f'<a href="{detail_url}">查看1001号用户</a>'
# 点击链接生成地址：/user/1001?source_page=user_list&page=3
# 场景 4：文件下载，携带下载标记与回调参数
# 后端下载接口，附带来源、文件类型参数做日志统计
# python
# 运行
# @app.route('/download/file')
# def download_file():
    # file_id = 88
    # # 下载链接附带统计参数：/download/file?file_id=88&from=report&token=xxx
    # download_link = url_for("download_file", file_id=file_id, from="report", token="abc123")
    # return f'<a href="{download_link}">下载报表</a>'
# 场景 5：登录 / 权限跳转，携带跳转后回跳地址
# 登录页常用：未登录访问需要权限的页面，跳登录，登录成功后返回原来页面
# python
# 运行
# @app.route('/login')
# def login():
    # # 获取跳转过来时携带的 next 目标地址
    # next_url = request.args.get("next", url_for("index"))
    # return f'''
    # <p>登录页面</p>
    # <a href="{next_url}">登录成功后返回</a>
    # '''

# @app.route('/admin')
# def admin():
    # # 需要登录，拼接 next 参数传递当前页面
    # login_redirect = url_for("login", next="/admin")
    # return f'无权限，请<a href="{login_redirect}">登录</a>'

# @app.route('/')
# def index():
    # return '首页'
# 访问 /admin 生成登录地址：/login?next=/admin
# 补充：和路由变量区分清楚
# python
# 运行
# # 路由带固定变量 <name>，必须放在url_for传参
# @app.route('/user/<name>')
# def user(name): pass

# # name 是路由占位变量，会拼进路径；sort、page是额外参数，拼 ? 查询串
# url_for("user", name="tom", sort="time", page=2)
# # 输出：/user/tom?sort=time&page=2
# 核心总结
# url_for(视图名, 路由变量=值, 任意自定义参数)
# 匹配路由 <xxx> 的参数：拼接进 URL 路径
# 其余参数：自动拼接为 ?k=v&k2=v2 查询字符串
# 业务中分页、搜索筛选、登录回跳、来源记录、下载统计全靠这个特性实现。