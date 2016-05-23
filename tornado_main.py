#!/usr/bin/env python

# Run this with
# PYTHONPATH=. DJANGO_SETTINGS_MODULE=testsite.settings testsite/tornado_main.py
# Serves by default at
# http://localhost:8080/hello-tornado and
# http://localhost:8080/hello-django

from tornado.options import options, define, parse_command_line
import django.core.handlers.wsgi
import tornado.httpserver
import tornado.ioloop
import tornado.autoreload
import tornado.web
import tornado.wsgi
import os
import sys
from django.conf import settings

from manage import initialize_settings

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "libs"))
try:
    port = int(sys.argv[1])
except IndexError:
    port = 8000
define('port', type=int, default=port)


class HelloHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('Hello from tornado')


def main():
    wsgi_app = tornado.wsgi.WSGIContainer(
            django.core.handlers.wsgi.WSGIHandler())
    tornado_app = tornado.web.Application(
            [
                (r"/static/(.*)", tornado.web.StaticFileHandler, {"path": settings.STATIC_ROOT}),
                ('.*', tornado.web.FallbackHandler, dict(fallback=wsgi_app)),
            ])
    server = tornado.httpserver.HTTPServer(tornado_app)
    server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
    '''
  loop=tornado.ioloop.IOLoop.instance() 
  tornado.autoreload.start(loop)
  print "Starting server on: %d"%int(port)
  loop.start()
  '''


if __name__ == '__main__':
    # os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rootapp.settings")
    initialize_settings()
    main()
