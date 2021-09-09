from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask('app')


@app.route('/')
def home():
    return render_template('index.html')


app.run(host='0.0.0.0', port=8080, debug=True)
