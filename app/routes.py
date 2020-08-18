import os.path
import markdown
import markdown.extensions.fenced_code

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
    basemdl = os.path.join(BASE_DIR, 'static/nlweb/basenlweb.html')
    mdl = os.path.join(BASE_DIR, 'static/nlogo/' + pn +'.nlogo')
    
    if os.path.exists(md):
        with open(md, 'r') as d: 
            description_rendered = markdown.markdown(d.read(), extensions=["fenced_code"])
            if os.path.exists(mdl):
                with open(mdl, 'r') as m:
                    full_model = m.read().replace('`', '\`')
                    code = full_model.split("@#$#@#$#@")[0] 
                    ## that string of characters separates the sections of a .nlogo file, 
                    ## the first of which is the code itself.
                    with open(basemdl, 'r') as bm:
                        return render_template('primitive.html', 
                                                primitive = pn, 
                                                description = description_rendered, 
                                                code = code, 
                                                basemodel = bm.read(), 
                                                model = full_model)
            else:
                return "TODO: create a template for a description without a model (example: inspect)"
    else:
        ## MAKE THIS RENDER A 404 File!!!
        return 'I don\'t know what ' + pn + ' is :('
            