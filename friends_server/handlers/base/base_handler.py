#coding=utf-8
import tornado.escape
from pycket.session import SessionMixin
import tornado.websocket
import tornado.web
from libs.db.dbsession import dbSession
from models.friends.friends_model import User1


class BaseHandler(tornado.web.RequestHandler, SessionMixin):
    def initialize(self):
        self.db=dbSession

    def get_current_user(self):
        if self.session.get("user_name"):
            return User1.by_name(self.session.get("user_name"))
        else:
            return None

    def on_finish(self):
        self.db.close()


class BaseWebSocket(tornado.websocket.WebSocketHandler, SessionMixin):
    def get_current_user(self):
        if self.session.get("user_name"):
            return User1.by_name(self.session.get("user_name"))
        else:
            return None