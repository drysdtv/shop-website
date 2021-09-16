from flask import Flask, render_template, request, redirect, url_for, make_response
import sqlite3 as sql

app = Flask('app')

quantity1 = 0
quantity2 = 0
quantity3 = 0
quantity4 = 0


@app.route('/', methods=['POST', 'GET'])
def home():
    global quantity1
    global quantity2
    global quantity3
    global quantity4
    if request.method == 'POST':
        if request.form.get('watch1'):
            quantity1 += 1
            item = request.form.get('watch1')
            res = make_response(render_template('index.html'))
            res.set_cookie(item, str(quantity1))
            return res
        if request.form.get('watch2'):
            item = request.form.get('watch2')
            quantity2 += 1
            res = make_response(render_template('index.html'))
            res.set_cookie(item, str(quantity2))
            return res
        if request.form.get('watch3'):
            quantity3 += 1
            item = request.form.get('watch3')
            res = make_response(render_template('index.html'))
            res.set_cookie(item, str(quantity3))
            return res
        if request.form.get('watch4'):
            quantity4 += 1
            item = request.form.get('watch4')
            res = make_response(render_template('index.html'))
            res.set_cookie(item, str(quantity4))
            return res
    return render_template('index.html')


@app.route('/cart', methods=['POST', 'GET'])
def cart():
    global quantity1
    global quantity2
    global quantity3
    global quantity4
    if request.form.get('watch1'):
        quantity1 = 0
        item = request.form.get('watch1')
        res = make_response(render_template('cart.html'))
        res.set_cookie(item, str(quantity1), max_age=0)
        return res
    if request.form.get('watch2'):
        quantity2 = 0
        item = request.form.get('watch2')
        res = make_response(render_template('cart.html'))
        res.set_cookie(item, str(quantity2), max_age=0)
        return res
    if request.form.get('watch3'):
        quantity3 = 0
        item = request.form.get('watch3')
        res = make_response(render_template('cart.html'))
        res.set_cookie(item, str(quantity3), max_age=0)
        return res
    if request.form.get('watch4'):
        quantity4 = 0
        item = request.form.get('watch4')
        res = make_response(render_template('cart.html'))
        res.set_cookie(item, str(quantity4), max_age=0)
        return res
    return render_template('cart.html')


@app.route('/cookie/')
def cookie():
    if not request.cookies.get('cart'):
        res = make_response("Setting a cookie")
        res.set_cookie('cart', 'watch1')
    else:
        res = make_response("Value of cookie foo is {}".format(request.cookies.get('cart')))
    return res, render_template('cookie.html')


app.run(host='0.0.0.0', port=8080, debug=True)
