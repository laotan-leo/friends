#coding=utf-8
import tornado.httpserver
import tornado.web
import tornado.ioloop
import tornado.escape
from tornado.options import define, options
from handlers.main.main_urls import handlers
from config import settings
from libs.db import create_talbes
from models.admin.permission_model import Employee
from libs.db.dbsession import dbSession
#定义一个默认的端口
define("port", default=8000, help="run port ", type=int)
define("t",  default=False, help="creat tables", type=bool)
define("a",  default=False, help="creat tables", type=bool)
define("s", default=False, help="creat tables", type=bool)

def create_super_admin():
    emp = Employee()
    emp.username = "superamdin"
    emp.password = '222'
    dbSession.add(emp)
    dbSession.commit()


if __name__ == "__main__":
    options.parse_command_line()
    if options.t:
        create_talbes.run()
    if options.a:
        print '你好请使用我们的系统...'
    if options.s:
        create_super_admin()
        print '超级管理员创建成功'


    app = tornado.web.Application(handlers, **settings)

    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    print 'start server...'
    tornado.ioloop.IOLoop.instance().start()
