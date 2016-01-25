from bottle import route

@route('/manager')
def index():
    return 'manager'
