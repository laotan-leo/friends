#coding=utf-8
from admin_handler import has_permission

def menu_permission(self, menu):

    if has_permission(self, menu):
        return True
    return False


