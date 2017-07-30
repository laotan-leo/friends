#coding=utf-8
from main_handler import MainHandler
from handlers.friends.friends_urls import friends_urls
from handlers.public.admin_accounts.admin_urls import admin_accounts_urls
from handlers.websocket.websocket_urls import websocket_urls
from handlers.blog.blog_urls import blog_urls
from handlers.admin.admin_urls import admin_urls


handlers = [
    (r'/', MainHandler),
]

handlers += friends_urls
handlers += admin_accounts_urls
handlers += websocket_urls
handlers += blog_urls
handlers += admin_urls
