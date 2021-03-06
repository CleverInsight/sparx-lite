"""
`Sparx Lite Server`
Author: @bastinrobin
"""
import os
import logging
from version import version
import tornado.ioloop
import tornado.web
from tornado.options import options
from config import SETTINGS
from controllers import MainHandler, DocsHandler, \
LoginHandler, LogoutHandler, TemplateHandler



class Application(tornado.web.Application):
    ''' Application Route Declaration '''
    def __init__(self):

        handlers = [

            (r"/", MainHandler),
            (r"/docs", DocsHandler),
            (r"/login", LoginHandler),
            (r"/logout", LogoutHandler),
            (r"/(.*)", TemplateHandler)
        ]

        tornado.web.Application.__init__(self, handlers, **SETTINGS)


def start_app():

    ''' Sparx server instantiation'''
    tornado.options.parse_command_line()
    app = Application()
    app.listen(options.port)
    logging.info('*** Sparx-lite - version '+ str(version) +'. started at:\
     http://localhost:%d/' % (options.port))
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    start_app()
