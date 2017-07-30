#coding=utf-8
from handlers.base.base_handler import BaseHandler
from models.friends.friends_model import User1

class ModifyNameHandler(BaseHandler):

    def get(self):
        user = User1.by_uuid(self.get_argument('uuid', ''))
        self.db.delete(user)
        self.db.commit()
        self.redirect('/')


    def post(self):
        user = User1.by_uuid(self.get_argument('uuid', ''))
        delete = self.get_argument('delete', '')
        if delete == 'delete':
            self.db.delete(user)
            self.db.commit()
            self.redirect('/')
        elif user:
            user.username=self.get_argument('username', '')
            self.db.add(user)
            self.db.commit()
            self.redirect('/')
        else:
            self.write('error no')