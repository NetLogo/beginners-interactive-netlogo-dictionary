import os.path
import random
import markdown
import markdown.extensions.fenced_code
import json
from string import ascii_lowercase, ascii_uppercase

from flask import abort, redirect, render_template, request, url_for
from markupsafe import escape
from app import app



@app.route('/')
@app.route('/index')
@app.route('/index.html')
def index():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    
    # open the video file
    vfile = os.path.join(BASE_DIR, 'static/videos.json')
    # load the videos as json object and pick 4 of them randomly
    with open(vfile, 'r') as vf:
        v = json.load(vf)

    v_all = v['videos']
    v_main_page = [video for video in v_all if video['should_show_on_main_page'] == True] 
    
    # now open the articles file
    afile = os.path.join(BASE_DIR, 'static/articles.json')
    with open(afile, 'r') as af:
        a = json.load(af)

    a_all = a['articles']
    a_main_page = [ad for ad in a_all if ad['should_show_on_main_page'] == True] 

    return render_template('index.html', 
                            videos = v_all, ## TODO: CHANGE BACK TO v_main_page & a_main_page
                            articles=a_all, 
                            title="NetLogo Interactive Dictionary")
    
@app.route('/dictionary')
@app.route('/dictionary.html')
def dictionary():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    dfile = os.path.join(BASE_DIR, 'static/primitives.json')
    with open(dfile, 'r') as df:
        d = json.load(df)
        return render_template('dictionary.html', letters = ascii_uppercase, dictionary = d, title="Explore the NetLogo Dictionary")
    
@app.route('/primitive/<primitive_name>', methods = ['GET'])
@app.route('/primitive/<primitive_name>.html', methods = ['GET'])
def primitive(primitive_name):
    
    primitive_name = escape(primitive_name)
    
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    dfile = os.path.join(BASE_DIR, 'static/primitives.json')
    modelslistfile = os.path.join(BASE_DIR, 'static/modelslist.txt')
    md = os.path.join(BASE_DIR, 'static/md/' + primitive_name +'.md')
    nlcode = os.path.join(BASE_DIR, 'static/nlcode/' + primitive_name +'.nlcode')
    basemdl = os.path.join(BASE_DIR, 'static/nlweb/basenlweb.html')
    mdl = os.path.join(BASE_DIR, 'static/nlogo/' + primitive_name +'.nlogo')
    
    if os.path.exists(md):
        with open(dfile, 'r') as df:
            primitives = json.load(df)["primitives"]
        if primitive_name not in primitives:
            abort(404)


        this_primitive = primitives[primitive_name]
        
        display_name = this_primitive["display_name"] if "display_name" in this_primitive else primitive_name
        
        see_also_names = this_primitive["see_also"] if "see_also" in this_primitive else []
        ## get full object entries for all primitives in the "see_also" list that we have entries for. 
        see_also = [primitives[name] for name in see_also_names if name in primitives] 
        
        library_models = this_primitive["library_models"] if "library_models" in this_primitive else []
        
        with open(md, 'r') as d: 
            description_rendered = markdown.markdown(d.read(), extensions=["fenced_code"])
        if os.path.exists(mdl):
            with open(mdl, 'r') as m:
                full_model = m.read().replace('`', '\`')
            code = full_model.split("\n@#$#@#$#@")[0] 
            ## that string of characters separates the sections of a .nlogo file, 
            ## the first of which is the code itself.
            
            with open(basemdl, 'r') as bm:
                basemodel = bm.read()
            return render_template('primitive.html', 
                                    primitive = primitive_name, 
                                    display_name = display_name,
                                    description = description_rendered, 
                                    code = code, 
                                    basemodel = basemodel, 
                                    model = full_model,
                                    title = display_name + " primitive",
                                    see_also = see_also,
                                    library_models = library_models)
        else:
            return render_template('primitive_no_model.html',
                                    primitive = display_name, 
                                    body=description_rendered, 
                                    title= display_name + " primitive",
                                    see_also = see_also,
                                    library_models = library_models)
    else:
        ## MAKE THIS RENDER A 404 File!!!
        abort(404) ## update the error message maybe?
            
@app.route('/search', methods = ['GET'])
@app.route('/search.html', methods = ['GET'])
def search():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    dfile = os.path.join(BASE_DIR, 'static/primitives.json')
    with open(dfile, 'r') as df:
        d = json.load(df)
    return render_template('search.html', dictionary = d, title = "Search results")
    
@app.route('/article/<article_name>', methods = ['GET'])
@app.route('/article/<article_name>.html', methods = ['GET'])
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

@app.route('/articles')
@app.route('/articles.html')
def articles():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    afile = os.path.join(BASE_DIR, 'static/articles.json')
    with open(afile, 'r') as af:
        a = json.load(af)
    return render_template('articles.html', articles = a['articles'], title="Articles and Guides")

@app.route('/videos')
@app.route('/videos.html')
def videos():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    vfile = os.path.join(BASE_DIR, 'static/videos.json')
    with open(vfile, 'r') as vf:
        v = json.load(vf)
        
    return render_template('videos.html', videos = v['videos'], title="Videos")
    
@app.route('/watch/<video_name>', methods = ['GET'])
@app.route('/watch/<video_name>.html', methods = ['GET'])
def watch(video_name):
    vn = escape(video_name)
    
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    vfile = os.path.join(BASE_DIR, 'static/videos.json')
    with open(vfile, 'r') as vf:
        v = json.load(vf)
    vdata = list(filter(lambda x:x["href"]==vn+".mp4",v["videos"]))
    return render_template('watch.html', vid = vn, title = vdata[0]["title"], description = vdata[0]["short_description"])
