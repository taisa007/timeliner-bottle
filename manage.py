from bottle import run

import user.views
import manager.views

run(host='localhost', port=8080)
