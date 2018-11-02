from flask import Flask

app = Flask(__name__) #实例化flask

#路由地址 根据用户不同的url进行处理
@app.route('/')
def index():#处理当前请求的函数
    return 'Hello Flask'

#http://127.0.0.1:5000/test/
@app.route('/test/') #路由地址末尾的/建议加上
def test():
    return '我是测试使用的视图函数'


@app.route('/page/<pagenum>/') #参数的语法格式 /路由名称/<形参名>/
def page(pagenum):
    return '当前的页码为{}'.format(pagenum)

if __name__ == '__main__':
    app.run() #运行当前的flask