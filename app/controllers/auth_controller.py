from bottle import template, get, post, redirect, request, hook

user = 'test'
passwd = 'pass'


@hook('before_request')
def setup_request():
    request.session = request.environ['beaker.session']


@get('/index')
def index():
    u = request.session['user_name']
    return template('users/index', username=u)


@get('/login')
def get_login():
    return template('users/login')


@post('/login')
def post_login():
    username = request.forms.get('username')
    password = request.forms.get('password')

    if username == user and passwd == password:
        # s = request.environ.get('beaker.session')
        request.session['user_name'] = username
        # s['user_name'] = username
        # s.save()
        request.session.save()
        return redirect('/')

    error = 'invalid'
    return template('users/login', error=error)
