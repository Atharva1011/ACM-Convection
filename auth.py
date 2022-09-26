from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return "<h1>LOGIN<>/h1"

@auth.route('/signup', methods=['GET', 'POST'])
def sign_up():
    return "<h1>LOGUT<>/h1"