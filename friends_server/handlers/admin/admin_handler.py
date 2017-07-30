#coding=utf-8
from handlers.base.base_handler import BaseHandler
from constants import ADMIN
import functools
import tornado.web
from models.admin.permission_model import (Permission, Role, Employee, Menu,
                                           EmployeeToRole,PermissionToRole)

def admin_auth(method):
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        if self.current_user:
            #判断session中的IP 和当前访问的ip是否一致
            if self.session.get('ip_address', '') == self.request.remote_ip:
                return method(self, *args, **kwargs)
            else:
                self.write("ip地址不符")
        else:
            self.redirect('/admin/adminlogin')
    return wrapper


def admin_ip_list(get):
    @functools.wraps(get)
    def aa(self, *args, **kwargs):
        if self.request.remote_ip in ADMIN:
            return get(self, *args, **kwargs)
        else:
            self.write('不在管理员列表中')
    return aa


def has_permission(self, name):
    # if name == "1":
    #     return True
    return True


def handler_permission(handlername):
    def func(get):
        @functools.wraps(get)
        def warpper(self, *args, **kwargs):
            if has_permission(self, handlername):
                return get(self, *args, ** kwargs)
            else:
                self.write("判断失败")
        return warpper
    return func



class AdminIndexHandler(BaseHandler):
    @admin_auth    #防止劫持攻击
    @admin_ip_list #白名单
    @handler_permission('AdminIndexHandler')
    def get(self):
        superadmin = self.db.query(Employee).filter(Employee.id ==1).first()
        for role in superadmin.roles:
            for permission in role.permissions:
                print permission.pname
        print '-------------------------------------------'
        menu = self.db.query(Menu).filter(Menu.menuname == 'menuboke').first()
        print menu.permission.pname




        self.render("admin/admin_index.html")



