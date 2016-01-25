from bottle import route, template, get, post, redirect


@get('/')
def index():
    return template('login')


@post('/')
def login():
    return redirect('/')
