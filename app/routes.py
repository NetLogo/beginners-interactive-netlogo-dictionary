import os.path

from flask import render_template, flash, redirect, request, url_for
from markupsafe import escape
from app import app



@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
    # return render_template('index.html', title='Landing page', user=user)
    
@app.route('/primitive/<primitive_name>', methods = ['GET'])
def primitive(primitive_name):
    
    pn = escape(primitive_name)
    
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    md = os.path.join(BASE_DIR, 'static/md/' + pn +'.md')
    nlcode = os.path.join(BASE_DIR, 'static/nlcode/' + pn +'.nlcode')
    mdl = os.path.join(BASE_DIR, 'static/nlweb/' + pn +'.html')
    
    if os.path.exists(md):
        with open(md, 'r') as d: 
            with open(nlcode, 'r') as nc:
                with open(mdl, 'r') as m:
                    return render_template('primitive.html', primitive = pn, description = d.read(), code = nc.read(), model = m.read())
    else:
        ## MAKE THIS RENDER A 404 File!!!
        return 'I don\'t know what ' + pn + ' is :('
            