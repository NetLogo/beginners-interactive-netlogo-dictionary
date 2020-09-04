import os
import json
from flask_frozen import Freezer
from app import app

freezer = Freezer(app)


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(BASE_DIR, 'app/static/primitives.json'), 'r') as df:
    primitivesJson = json.load(df)
primitivesViaJson = primitivesJson['primitives']
mdDir = os.path.join(BASE_DIR, 'app/static/md/')
primitivesViaMd = [filename[:-3] for filename in os.listdir(mdDir) if filename.endswith('.md')]

validPrimitives = [primitive for primitive in primitivesViaMd if primitive in primitivesViaJson]
    
@freezer.register_generator
def primitive():
    for primitive in validPrimitives:
        yield '/primitive/' + primitive + '.html'

articlesDir = os.path.join(BASE_DIR, 'app/static/articles')
articles = [filename[:-3] for filename in os.listdir(articlesDir) if filename.endswith('.md')]

@freezer.register_generator
def article():
    for article in articles:
        yield '/article/' + article + '.html'

with open(os.path.join(BASE_DIR, 'app/static/videos.json')) as videosJsonFile:
    videosJson = json.load(videosJsonFile)

videoFiles = [video['href'] for video in videosJson['videos']]
validVideoNames = [video[:-4] for video in videoFiles if video.endswith('.mp4')]

@freezer.register_generator
def watch():
    for video in validVideoNames:
        yield '/watch/' + video + '.html'
        

if __name__ == '__main__':
    #freezer.run(port=4141)
    #yay
    freezer.freeze()