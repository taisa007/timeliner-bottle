from bottle import template, get, post, redirect, request


@get('/')
def index():
    return template('users/index')
