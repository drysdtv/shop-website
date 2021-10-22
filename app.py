import flask_login
from flask import Flask, render_template, request, redirect, url_for, make_response, flash, session
import sqlite3 as sql
from wtforms import StringField, PasswordField, BooleanField, IntegerField
from wtforms.validators import InputRequired, Email, Length, NoneOf, AnyOf, NumberRange
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user, set_login_view
import models as dbh
import os
import string
import array

dbh.createDB()

x = str(os.urandom(32))

page = None
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
stock1 = 4
stock2 = 4
stock3 = 4
stock4 = 4
items = 0
admin = False

watchesCart = [
]


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


loginManager.login_view = "login"
loginManager.login_message = "please login before trying that"


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
    password = PasswordField('password', validators=[InputRequired(), Length(min=4, max=20, message='Please enter a password between 4 and 20 characters')])


class Paying(FlaskForm):
    cardNumber = IntegerField('number', validators=[InputRequired(), Length(min=12, max=12)])
    cvv = IntegerField('security', validators=[InputRequired(), Length(3), NumberRange(min=000, max=999)])
    name = StringField('name', validators=[InputRequired()])
    address = StringField('address', validators=[InputRequired()])
    location = StringField('location', validators=[InputRequired()])


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
    global page
    global watchesCart
    global stock1
    global stock2
    global stock3
    global stock4
    page = "index"
    if request.method == 'POST':
        if request.form.get('watch1'):
            quantity1 += 1
            stock1 -= 1
            p = len(watchesCart)
            if p == 0:
                watchesCart.insert(0,
                                   {"id": 1, 'name': request.form.get("watch1"), "quantity": quantity1, "stock": stock1,
                                    "price": 599})
            else:
                for i in range(len(watchesCart)):
                    if watchesCart[i].get("name") == request.form.get("watch1"):
                        watchesCart[i].update(
                            {'name': request.form.get("watch1"), "quantity": quantity1, "stock": stock1})
                        return render_template("index.html", watchesCart=watchesCart, loggedIn=loggedIn)
                print(len(watchesCart))
                watchesCart.insert(len(watchesCart), {"id": (len(watchesCart) + 1), 'name': request.form.get("watch1"),
                                                      "quantity": quantity1, "stock": stock1, "price": 599})
            return render_template("index.html", watchesCart=watchesCart, loggedIn=loggedIn)
        if request.form.get('watch2'):
            stock2 -= 1
            quantity2 += 1
            p = len(watchesCart)
            if p == 0:
                watchesCart.insert(0,
                                   {"id": 1, 'name': request.form.get("watch2"), "quantity": quantity2, "stock": stock2,
                                    "price": 599})
            else:
                for i in range(len(watchesCart)):
                    if watchesCart[i].get("name") == request.form.get("watch2"):
                        watchesCart[i].update({"quantity": quantity2, "stock": stock2})
                        return render_template("index.html", watchesCart=watchesCart, loggedIn=loggedIn)
                watchesCart.insert(len(watchesCart), {"id": (len(watchesCart) + 1), 'name': request.form.get("watch2"),
                                                      "quantity": quantity2, "stock": stock2, "price": 599})
            return render_template("index.html", watchesCart=watchesCart, loggedIn=loggedIn)
        if request.form.get('watch3'):
            quantity3 += 1
            stock3 -= 1
            p = len(watchesCart)
            if p == 0:
                watchesCart.insert(len(watchesCart),
                                   {"id": 1, 'name': request.form.get("watch3"), "quantity": quantity3, "stock": stock3,
                                    "price": 599})
            else:
                for i in range(len(watchesCart)):
                    if watchesCart[i].get("name") == request.form.get("watch3"):
                        watchesCart[i].update(
                            {'name': request.form.get("watch3"), "quantity": quantity3, "stock": stock3})
                        return render_template("index.html", watchesCart=watchesCart, loggedIn=loggedIn)
                print(len(watchesCart))
                watchesCart.insert(len(watchesCart), {"id": (len(watchesCart) + 1), 'name': request.form.get("watch3"),
                                                      "quantity": quantity3, "stock": stock3, "price": 599})
            return render_template("index.html", watchesCart=watchesCart, loggedIn=loggedIn)
        if request.form.get('watch4'):
            quantity4 += 1
            stock4 -= 1
            p = len(watchesCart)
            if p == 0:
                watchesCart.insert(0,
                                   {"id": 1, 'name': request.form.get("watch4"), "quantity": quantity4, "stock": stock4,
                                    "price": 599})
            else:
                for i in range(len(watchesCart)):
                    if watchesCart[i].get("name") == request.form.get("watch4"):
                        watchesCart[i].update(
                            {'name': request.form.get("watch4"), "quantity": quantity4, "stock": stock4})
                        return render_template("index.html", watchesCart=watchesCart, loggedIn=loggedIn)
                watchesCart.insert(len(watchesCart), {"id": (len(watchesCart) + 1), 'name': request.form.get("watch4"),
                                                      "quantity": quantity4, "stock": stock4, "price": 599})
            return render_template("index.html", watchesCart=watchesCart, loggedIn=loggedIn)
        if request.form.get('signout'):
            flask_login.logout_user()
            loggedIn = False
            return render_template("index.html")
    return render_template('index.html', loggedIn=loggedIn, admin=admin, watchesCart=watchesCart)


@app.route('/cart', methods=['POST', 'GET'])
def cart():
    global page, loggedIn, quantity1, quantity2, quantity3, quantity4, watchesCart, stock1, stock2, stock3, stock4, items
    page = "payment"
    items = 0
    for o in range(len(watchesCart)):
        items += watchesCart[o].get("quantity") * watchesCart[o].get("price")
    if request.method == 'POST':
        for x in range(len(watchesCart)):
            if str(watchesCart[x].get("id")) in request.form.keys():
                items -= watchesCart[x].get("quantity") * watchesCart[o].get("price")
                watchesCart[x].update({"quantity": (int(request.form[str(watchesCart[x].get("id"))]))})
                items += watchesCart[x].get("quantity") * watchesCart[x].get("price")
                return render_template("cart.html", watchesCart=watchesCart, items=items)
        if request.form.get('watch1'):
            quantity1 = 0
            stock1 = 4
            for i in range(len(watchesCart)):
                if watchesCart[(i - 1)].get("name") == request.form.get("watch1"):
                    watchesCart.pop((i - 1))
                    return redirect(url_for('cart'))
        if request.form.get('watch2'):
            quantity2 = 0
            stock2 = 4
            for i in range(len(watchesCart)):
                if watchesCart[i].get("name") == request.form.get("watch2"):
                    watchesCart.pop((i - 1))
                    return redirect(url_for('cart'))
        if request.form.get('watch3'):
            quantity3 = 0
            stock3 = 4
            for i in range(len(watchesCart)):
                if watchesCart[i].get("name") == request.form.get("watch3"):
                    watchesCart.pop((i - 1))
                    return redirect(url_for('cart'))
        if request.form.get('watch4'):
            quantity4 = 0
            stock4 = 4
            for i in range(len(watchesCart)):
                if watchesCart[i].get("name") == request.form.get("watch4"):
                    watchesCart.pop((i - 1))
                    return redirect(url_for('cart'))
    return render_template('cart.html', watchesCart=watchesCart, items=items)


@app.route('/login', methods=['POST', 'GET'])
def login():
    global quantity1, quantity2, quantity3, quantity4, loggedIn, admin, page
    form = LoginForm()
    if current_user.is_authenticated:
        loggedIn = True
        return redirect(url_for(page))
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
                    print(us.get_id())
                    if us.get_id() == '1' or us.get_id() == '2':
                        admin = True
                        page = "orders"
                    else:
                        admin = False
                    return redirect(url_for(page))
    return render_template('login.html', form=form)


@app.route('/sign', methods=['POST', 'GET'])
def sign():
    form = SignUp()
    if form.validate_on_submit():
        dbh.insertUser(form.username.data, form.email.data, form.password.data)
    return render_template('signup.html', form=form)


@app.route('/orders', methods=['POST', 'GET'])
def orders():
    global admin
    if admin is True:
        return render_template('admin.html', admin=admin)
    else:
        return redirect(url_for("login"))


@app.route('/payment', methods=['POST', 'GET'])
@login_required
def payment():
    form = Paying()
    return render_template("payment.html", form=form)


app.run(host='0.0.0.0', port=5000, debug=True)
