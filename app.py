from flask import Flask, render_template, request, redirect, url_for
import sqlite3
addCart1 = False


def addCart1(item):
    print(item)


app = Flask('app')


@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        if request.form.get("buy"):
            addCart1("buy")

    return render_template('index.html')


@app.route('/cart')
def cart():
    return render_template('cart.html')


app.run(host='0.0.0.0', port=8080, debug=True)
