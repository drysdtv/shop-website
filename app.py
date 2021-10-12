from flask import Flask, render_template, request, redirect, url_for, make_response, flash
import sqlite3 as sql
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length, NoneOf, AnyOf
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user
import models as dbh
import os
import string

dbh.createDB()

x = str(os.urandom(16))

app = Flask('app')
loggedIn = False
loginManager = LoginManager(app)
loginManager.login_view = "login"
bootstrap = Bootstrap(app)
app.secret_key = x
quantity1 = 0
quantity2 = 0
quantity3 = 0
quantity4 = 0


class User(UserMixin):
    def __init__(self, id, username, password):
        self.id = str(id)
        self.username = username
        self.password = password
        self.authenticated = False

    def is_active(self):
        return self.is_active()

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return self.authenticated

    def is_active(self):
        return True

    def get_id(self):
        return self.id


@loginManager.user_loader
def load_user(user_id):
    connection = sql.connect("website.db")
    cursor = connection.cursor()
    cursor.execute("select * from login where id = ?", [user_id])
    ting = cursor.fetchone()
    if ting is None:
        return render_template('login.html')
    else:
        return User(int(ting[0]), ting[1], ting[3])


class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=4, max=80)])
    remember = BooleanField('remember me')


class SignUp(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid Email'), Length(max=50)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=4, max=20,
                                                                             message='Please enter a password between 4 and 20 characters')])

@app.route('/')
def starting():
    return redirect(url_for("index"))


@app.route('/index', methods=['POST', 'GET'])
def index():
    global loggedIn
    global quantity1
    global quantity2
    global quantity3
    global quantity4
    if request.method == 'POST':
        if request.form.get('watch1'):
            quantity1 += 1
            item = request.form.get('watch1')
            res = make_response(redirect(url_for("index")))
            res.set_cookie(item, str(quantity1))
            dbh.addCart(str(item), 599, quantity1)
            return res
        if request.form.get('watch2'):
            item = request.form.get('watch2')
            quantity2 += 1
            res = make_response(redirect(url_for("index")))
            res.set_cookie(item, str(quantity2))
            dbh.addCart(item, 599, quantity2)
            return res
        if request.form.get('watch3'):
            quantity3 += 1
            item = request.form.get('watch3')
            res = make_response(redirect(url_for("index")))
            res.set_cookie(item, str(quantity3))
            dbh.addCart(item, 599, quantity3)
            return res
        if request.form.get('watch4'):
            quantity4 += 1
            item = request.form.get('watch4')
            res = make_response(redirect(url_for("index")))
            res.set_cookie(item, str(quantity4))
            dbh.addCart(item, 599, quantity4)
            return res
        if request.form.get('signout'):
            print('good')
    return render_template('index.html', loggedIn=loggedIn)


@app.route('/cart', methods=['POST', 'GET'])
def cart():
    global loggedIn
    x1 = request.cookies.get('watch1')
    x2 = request.cookies.get('watch2')
    x3 = request.cookies.get('watch3')
    x4 = request.cookies.get('watch4')
    global quantity1
    global quantity2
    global quantity3
    global quantity4
    if request.method == 'POST':
        if request.form.get("q1"):
            u1 = int(request.form["q1"])
            quantity1 = u1
        if request.form.get("q2"):
            u1 = int(request.form["q2"])
            quantity2 = u1
        if request.form.get("q3"):
            u1 = int(request.form["q3"])
            quantity3 = u1
        if request.form.get("q4"):
            u1 = int(request.form["q4"])
            quantity4 = u1

    if request.form.get('watch1'):
        quantity1 = 0
        item = request.form.get('watch1')
        res = make_response(
            render_template('cart.html', x1=x1, x2=x2, x3=x3, x4=x4, quantity1=quantity1, quantity2=quantity2, quantity3=quantity3, quantity4=quantity4, loggedIn=loggedIn))
        res.set_cookie(item, str(quantity1), max_age=0)
        return res
    if request.form.get('watch2'):
        quantity2 = 0
        item = request.form.get('watch2')
        res = make_response(
            render_template('cart.html', x1=x1, x2=x2, x3=x3, x4=x4, quantity1=quantity1, quantity2=quantity2, quantity3=quantity3, quantity4=quantity4, loggedIn=loggedIn))
        res.set_cookie(item, str(quantity2), max_age=0)
        return res
    if request.form.get('watch3'):
        quantity3 = 0
        item = request.form.get('watch3')
        res = make_response(
            render_template('cart.html', x1=x1, x2=x2, x3=x3, x4=x4, quantity1=quantity1, quantity2=quantity2, quantity3=quantity3, quantity4=quantity4, loggedIn=loggedIn))
        res.set_cookie(item, expires=0)
        return res
    if request.form.get('watch4'):
        quantity4 = 0
        item = request.form.get('watch4')
        res = make_response(
            render_template('cart.html', x1=x1, x2=x2, x3=x3, x4=x4, quantity1=quantity1, quantity2=quantity2, quantity3=quantity3, quantity4=quantity4, loggedIn=loggedIn))
        res.set_cookie(item, str(quantity4), max_age=0)
        return res
    return render_template('cart.html', x1=x1, x2=x2, x3=x3, x4=x4, quantity1=quantity1, quantity2=quantity2, quantity3=quantity3, quantity4=quantity4, loggedIn=loggedIn)


@app.route('/login', methods=['POST', 'GET'])
def login():
    x1 = request.cookies.get('watch1')
    x2 = request.cookies.get('watch2')
    x3 = request.cookies.get('watch3')
    x4 = request.cookies.get('watch4')
    global quantity1
    global quantity2
    global quantity3
    global quantity4
    global loggedIn
    form = LoginForm()
    if current_user.is_authenticated:
        loggedIn = True
        return render_template('index.html', loggedIn=loggedIn)
    if form.validate_on_submit():
        con = sql.connect("website.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM login where username = ?", [form.username.data])
        user = cur.fetchone()
        if user is None:
            fail = True
            return render_template('login.html', fail=fail, form=form)
        else:
            us = load_user(user[0])
            if form.username.data == us.username:
                if form.password.data == us.password:
                    login_user(us, remember=form.remember.data)
                    loggedIn = True
                    return render_template('cart.html', loggedIn=loggedIn, name=us.username, x1=x1, x2=x2, x3=x3, x4=x4, quantity1=quantity1, quantity2=quantity2, quantity3=quantity3, quantity4=quantity4)
    return render_template('login.html', form=form)


@app.route('/sign', methods=['POST', 'GET'])
def sign():
    form = SignUp()
    if form.validate_on_submit():
        dbh.insertUser(form.username.data, form.email.data, form.password.data)
    return render_template('signup.html', form=form)


app.run(host='0.0.0.0', port=5000, debug=True)
