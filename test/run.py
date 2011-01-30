#!/usr/bin/env python
import os

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.autoreload

import api

from tornado.options import define, options

define("port", default=9999, help="run on the given port", type=int)
define("processes", default=4, help="number of threads in the pool", type=int)

class TestApp(tornado.web.Application):
    def __init__(self,ioloop):
        handlers = [
            (r"/", api.TestHandler),
        ]
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            debug=True,
            io_loop=ioloop
        )
        tornado.web.Application.__init__(self, handlers, **settings)


def main():
    tornado.options.parse_command_line()
    ioloop = tornado.ioloop.IOLoop.instance()
    http_server = tornado.httpserver.HTTPServer(TestApp(ioloop))
    http_server.listen(options.port)
    tornado.autoreload.start()
    ioloop.start()

if __name__ == "__main__":
    main()
