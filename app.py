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
    x1 = request.cookies.get('watch1')
    x2 = request.cookies.get('watch2')
    x3 = request.cookies.get('watch3')
    x4 = request.cookies.get('watch4')
    global quantity1
    global quantity2
    global quantity3
    global quantity4
    if request.form.get('watch1'):
        quantity1 = 0
        item = request.form.get('watch1')
        res = make_response(render_template('cart.html', x1=x1, x2=x2, x3=x3, x4=x4, quantity1=quantity1, quantity2=quantity2, quantity3=quantity3, quantity4=quantity4))
        res.set_cookie(item, str(quantity1), max_age=0)
        return res
    if request.form.get('watch2'):
        quantity2 = 0
        item = request.form.get('watch2')
        res = make_response(render_template('cart.html', x1=x1, x2=x2, x3=x3, x4=x4,quantity1=quantity1, quantity2=quantity2, quantity3=quantity3, quantity4=quantity4))
        res.set_cookie(item, str(quantity2), max_age=0)
        return res
    if request.form.get('watch3'):
        quantity3 = 0
        item = request.form.get('watch3')
        res = make_response(render_template('cart.html', x1=x1, x2=x2, x3=x3, x4=x4,quantity1=quantity1, quantity2=quantity2, quantity3=quantity3, quantity4=quantity4))
        res.set_cookie(item, str(quantity3), max_age=0)
        return res
    if request.form.get('watch4'):
        quantity4 = 0
        item = request.form.get('watch4')
        res = make_response(render_template('cart.html', x1=x1, x2=x2, x3=x3, x4=x4,quantity1=quantity1, quantity2=quantity2, quantity3=quantity3, quantity4=quantity4))
        res.set_cookie(item, str(quantity4), max_age=0)
        return res
    return render_template('cart.html', x1=x1, x2=x2, x3=x3, x4=x4,quantity1=quantity1, quantity2=quantity2, quantity3=quantity3, quantity4=quantity4)


app.run(host='0.0.0.0', port=5000, debug=True)
