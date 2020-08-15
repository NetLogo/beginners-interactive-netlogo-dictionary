from flask import render_template, flash, redirect, request, url_for
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
    # return render_template('index.html', title='Landing page', user=user)