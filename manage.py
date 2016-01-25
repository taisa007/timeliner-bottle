# -*- coding: utf-8 -*-

from bottle import run, route, static_file, default_app
from app.controllers import *
from beaker.middleware import SessionMiddleware

session_opts = {
    'session.type': 'file',
    'session.cookie_expires': 300,
    'session.data_dir': './data',
    'session.auto': True
}

app = default_app()
app = SessionMiddleware(app, session_opts)

@route('/static/<filepath:path>')
def static(filepath):
    return static_file(filepath, root='./static')

run(app=app, host='localhost', port=8080, debug=True, reloader=True)
