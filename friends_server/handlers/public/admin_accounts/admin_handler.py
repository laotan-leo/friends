#coding=utf-8
from datetime import datetime
from handlers.public.error.error import AuthError
from handlers.base.base_handler import BaseHandler
from models.friends.friends_model import User1


class AdminLoginHandler(BaseHandler):
    def get(self):
        self.render("public/admin_accounts/admin_login.html", nextname=self.get_argument("next", "/"))

    def post(self):
        user = User1.by_name(self.get_argument('name', ''))
        password = self.get_argument("password", "")
        remember = self.get_argument("remember", '')
        print remember
        if not user.locked:
            if user and user.auth_password(password):
                self.success_login(user)
                if user.loginnum == 1:
                    self.write('newuser.html')
                else:
                    self.redirect("/admin")
            else:
                self.write("登录失败")
        else:
            self.write("此用户已经被锁定，请联系管理员")

    def success_login(self, user):
        print user.username
        user.last_login = datetime.now()
        user.loginnum += 1
        self.db.add(user)
        self.db.commit()
        self.session.set('user_name', user.username)
        self.session.set('ip_address', self.request.remote_ip)


class AdminLoginOutHandler(BaseHandler):
    def get(self):
        self.session.delete("user_name")
        self.redirect("/admin/adminlogin")



class AdminLockScreenHandler(BaseHandler):
    def get(self):
        self.render('public/admin_accounts/admin_lock_screen.html')

    def post(self):
        if self._check_argument():
            self.redirect('/admin')
        else:
            self.render('public/admin_accounts/admin_lock_screen.html')

    def _check_argument(self):
        password = self.get_argument('password', '')
        return True if self.current_user.auth_password(password) else False



