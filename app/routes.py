import os.path
import markdown
import markdown.extensions.fenced_code
import json
from string import ascii_lowercase, ascii_uppercase

from flask import abort, redirect, render_template, request, url_for
from markupsafe import escape
from app import app



@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
    # return render_template('index.html', title='Landing page', user=user)
    
@app.route('/dictionary')
def dictionary():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    dfile = os.path.join(BASE_DIR, 'static/primitives.json')
    with open(dfile, 'r') as df:
        d = json.load(df)
        return render_template('dictionary.html', letters = ascii_uppercase, dictionary = d, title="Explore the NetLogo Dictionary")
    
@app.route('/primitive/<primitive_name>', methods = ['GET'])
def primitive(primitive_name):
    
    primitive_name = escape(primitive_name)
    
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    dfile = os.path.join(BASE_DIR, 'static/primitives.json')
    md = os.path.join(BASE_DIR, 'static/md/' + primitive_name +'.md')
    nlcode = os.path.join(BASE_DIR, 'static/nlcode/' + primitive_name +'.nlcode')
    basemdl = os.path.join(BASE_DIR, 'static/nlweb/basenlweb.html')
    mdl = os.path.join(BASE_DIR, 'static/nlogo/' + primitive_name +'.nlogo')
    
    if os.path.exists(md):
        with open(dfile, 'r') as df:
            primitives = json.load(df)["primitives"]
            
            display_name = primitives[primitive_name]["display_name"] if primitive_name in primitives else primitive_name
            
            see_also_names = primitives[primitive_name]["see_also"]
            see_also = [primitives[name] for name in see_also_names if name in primitives]
            
            with open(md, 'r') as d: 
                description_rendered = markdown.markdown(d.read(), extensions=["fenced_code"])
                if os.path.exists(mdl):
                    with open(mdl, 'r') as m:
                        full_model = m.read().replace('`', '\`')
                        code = full_model.split("\n@#$#@#$#@")[0] 
                        ## that string of characters separates the sections of a .nlogo file, 
                        ## the first of which is the code itself.
                        
                        with open(basemdl, 'r') as bm:
                            return render_template('primitive.html', 
                                                    primitive = primitive_name, 
                                                    display_name = display_name,
                                                    description = description_rendered, 
                                                    code = code, 
                                                    basemodel = bm.read(), 
                                                    model = full_model,
                                                    title = display_name + " primitive",
                                                    see_also = see_also)
                else:
                    return render_template('primitive_no_model.html',
                                            primitive = display_name, 
                                            body=description_rendered, 
                                            title= display_name + " primitive",
                                            see_also = see_also)
    else:
        ## MAKE THIS RENDER A 404 File!!!
        abort(404) ## update the error message maybe?
            
@app.route('/search', methods = ['GET'])
def search():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    dfile = os.path.join(BASE_DIR, 'static/primitives.json')
    with open(dfile, 'r') as df:
        d = json.load(df)
        return render_template('search.html', dictionary = d, title = "Search results")
    
@app.route('/article/<article_name>', methods = ['GET'])
def article(article_name):
    an = escape(article_name)
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    afile = os.path.join(BASE_DIR, 'static/articles/' + an +'.md')
    if os.path.exists(afile):
        with open(afile, 'r') as af:
            maf = markdown.markdown(af.read(), extensions=["fenced_code"])
            maf = maf.replace('<h1>', '<h1 class="display-4">') # just to make it look nicer
            return render_template('article.html', body = maf, title=an.replace('-', ' ').title())
    else:
        abort(404)  ## update the error message maybe?
    
    
@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404