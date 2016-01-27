# -*- coding: utf-8 -*-

from bottle import template, get, post, redirect, request, hook, jinja2_template, route, app

user = 'test'
passwd = 'pass'


@hook('before_request')
def setup_request():
    request.session = request.environ['beaker.session']


@get('/')
@get('/index')
def index():
    uname = request.session.get('user_name')

    tweet = {
        'id': '1',
        'tweet': 'tweet'
    }

    tweets = (tweet, tweet)

    return jinja2_template('users/index',
                           uname=uname,
                           tweets=tweets
                           )


@get('/login')
def get_login():
    return jinja2_template('users/login')


@post('/login')
def post_login():
    username = request.forms.get('username')
    password = request.forms.get('password')

    if username == user and passwd == password:
        request.session['user_name'] = username
        request.session.save()
        return redirect('/')

    error = 'invalid'
    return jinja2_template('users/login', error=error)


@get('/signup')
def get_signup():
    return jinja2_template('users/signup')


@post('/signup')
def post_signup():
    # DBに保存
    username = request.forms.get('username')
    password = request.forms.get('password')

    request.session['user_name'] = username
    request.session.save()

    return redirect('/')


@post('/logout')
def get_logout():
    request.session['user_name'] = None
    request.session.save()
    return redirect('/login')
