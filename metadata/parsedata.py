import json
import csv
import urllib.request
import io
import sys
import re
import os
import datetime
import pandas as pd
from PIL import Image

## constants
STAGING_JSON_PATH = "./staging/"
PRODUCTION_JSON_PATH = "../app/static/"
MODEL_IMGS_PATH = "../app/static/img/models/"
MODELS_LIBRARY_URL = "http://ccl.northwestern.edu/netlogo/models/"

PRIMITIVES_FILE_NAME = "primitives.json"
ARTICLES_FILE_NAME = "articles.json"
VIDEOS_FILE_NAME = "videos.json"

## CLI Options
verbose              = False
verboser             = False
production           = False
output_path          = STAGING_JSON_PATH
outputtingPrimitives = False
outputtingArticles   = False
outputtingVideos     = False
outputtingPictures   = False

## staging file -- for checking 
# outputFile = "./staging.json"

## actual primitives file
outputFile = "../app/static/primitives.json"

def populatePrimitives():
    if(verbose):
        print("### Starting to pull data for the primitives ###")
        
    out = {"primitives" : {}}
    primitives = out["primitives"]
    csv_filename = "csv/bind_primitives.csv"
    
    # first, let's convert the first sheet of the excel file to a csv file
    df = pd.DataFrame(pd.read_excel("binddata.xlsx", sheet_name=0))
    df.to_csv(csv_filename, index=False)

    with open(csv_filename, 'r') as csvfile:
        ## read the header line before parsing
        csvfile.readline() 

        reader = csv.reader(csvfile, delimiter = ",", quotechar='"')
        for row in reader:
            display_name = row[0]
            name = display_name
            if name.endswith("?"):
                name = name[:-1]
            
            short_description = row[1]
            
            search_terms = []
            if row[2] != "":
                search_terms = [term.strip() for term in row[2].split(',')]
            
            agents = []
            if row[3] == "True":
                agents.append("observer")
            if row[4] == "True":
                agents.append("turtles")
            if row[5] == "True":
                agents.append("patches")
            if row[6] == "True":
                agents.append("links")
            if row[7] == "True":
                agents.append("utilities")
            
            see_also = []
            if row[8] != "":
                see_also = [term.strip() for term in row[8].split(',')]
            
            library_models = []
            if row[9] != "":
                library_models = [term.strip() for term in row[9].split(',')]


            primitives[name] = {
                "identity" : name,
                "display_name" : display_name,
                "short_description" : short_description,
                "search_terms" : search_terms,
                "agents" : agents, 
                "see_also" : see_also,
                "library_models": library_models
            }
            if verboser:
                print(name, ":", primitives[name])

    ## dump to file
    if(verbose):
        print("dumping to " + output_path + PRIMITIVES_FILE_NAME)
    with open(output_path + PRIMITIVES_FILE_NAME, 'w') as outfile:
        json.dump(out, outfile, indent=4)
    if(verbose):
        print("Finished with primitives")

def processArticles():
    if(verbose):
        print("### Starting to pull data for articles ###")

    out = {"articles" : []}
    articles = out["articles"]
    csv_filename = "csv/bind_articles.csv"
    
    # first, let's convert the first sheet of the excel file to a csv file
    df = pd.DataFrame(pd.read_excel("binddata.xlsx", sheet_name=1))
    df.to_csv(csv_filename, index=False)

#    for page in ARTICLES_PAGES:
#        urlToOpen = "https://docs.google.com/spreadsheets/d/" + sheetUID + "/export?format=csv&gid=" + str(page)
#        if(verbose):
#            print("Starting on: " + urlToOpen)
#        ## make a http request and convert it into a string file object representation
#        HTTPResponse = urllib.request.urlopen(urlToOpen)
#        csvBytes = io.BytesIO(HTTPResponse.read())
#        csvfile = io.TextIOWrapper(csvBytes, encoding="utf-8")

    with open("csv/bind_articles.csv", 'r') as csvfile:

        ## read the header line before parsing
        csvfile.readline() 

        reader = csv.reader(csvfile, delimiter = ",", quotechar='"')
        for row in reader:
            title                       = row[0]
            href                        = row[1]
            short_description           = row[2]
            article_type                = row[3]
            should_show_on_main_page    = True if row[4].upper() == "TRUE" else False

            new_article = {
                    "title"                     : title,
                    "href"                      : href,
                    "short_description"         : short_description,
                    "type"                      : article_type,
                    "should_show_on_main_page"  : should_show_on_main_page
                }

            if verboser:
                print(new_article)
            articles.append(new_article)

    if verbose:
        print("dumping to " + output_path + ARTICLES_FILE_NAME)
    with open(output_path + ARTICLES_FILE_NAME, 'w') as outfile:
        json.dump(out, outfile, indent=4)
    if verbose:
        print("finished with articles")


def processVideos():
    if(verbose):
        print("### Starting to pull data for videos ###")
    
    out = {"videos" : []}
    videos = out["videos"]
    csv_filename = "csv/bind_videos.csv"
    
    # first, let's convert the first sheet of the excel file to a csv file
    df = pd.DataFrame(pd.read_excel("binddata.xlsx", sheet_name=0))
    df.to_csv(csv_filename, index=False)

    with open("bind_videos.csv", 'r') as csvfile:

        ## read the header line before parsing
        csvfile.readline() 

        reader = csv.reader(csvfile, delimiter = ",", quotechar='"')
        for row in reader:
            title                       = row[0]
            href                        = row[1]
            short_description           = row[2]
            should_show_on_main_page    = True if row[3] == "TRUE" else False

            new_video = {
                "title"                     : title,
                "href"                      : href,
                "short_description"         : short_description,
                "should_show_on_main_page"  : should_show_on_main_page
            }

            if verboser:
                print(new_video)
            videos.append(new_video)
        
        if verbose:
            print("dumping to " + output_path + VIDEOS_FILE_NAME)
        with open(output_path + VIDEOS_FILE_NAME, 'w') as outfile:
            json.dump(out, outfile, indent=4)
        if verbose:
            print("finished with videos")

def processPictures():
    if verbose:
        print("### Starting to pull pictures ###")

    with open(PRODUCTION_JSON_PATH + PRIMITIVES_FILE_NAME, 'r') as primitivesFile:
        j = json.load(primitivesFile)
        primitives = j["primitives"]

    ## every model referenced in the production primitives.json file
    modelsUsedInPrimitives = [item for primitive in primitives for item in primitives[primitive]['library_models']]
    modelNamesNoSpaces = map(lambda s: s.replace(' ', ''), set(modelsUsedInPrimitives))
    modelLinks = map(lambda s: "http://ccl.northwestern.edu/netlogo/models/" + s, modelNamesNoSpaces)

    if verbose:
        print("Got the list of all the urls to the models")

    imgTagRegex = re.compile('<img width=200 height=200 .+>')
    srcRegex = re.compile('(?<=src=").+(?=">)')
    fileNameRegex = re.compile('(?<=\/)[^/]+png$')
    urlDecodeRegex = re.compile('%20')

    num_total_imgs = 0
    num_new_downloaded = 0

    for modelLink in modelLinks:
        with urllib.request.urlopen(modelLink) as modelPageResponse:
            num_total_imgs += 1
            
            modelPageSource = modelPageResponse.read().decode('utf-8')
            # print(modelPageSource)
            imgTag = re.search(imgTagRegex, modelPageSource)
            if imgTag:
                imgSRC = "http://ccl.northwestern.edu/netlogo/" + re.search(srcRegex, imgTag.group(0)).group(0)
                imgName = re.search(fileNameRegex, re.sub(urlDecodeRegex, "", imgSRC)).group(0)
                imgDestination = MODEL_IMGS_PATH + imgName

                imgHeadRequest = urllib.request.Request(imgSRC, method='HEAD')
                response =  urllib.request.urlopen(imgHeadRequest)
                responseModifiedTimeStr = response.info().get('Last-Modified')
                ## see https://stackoverflow.com/a/1472008/6141684
                responseModifiedTime = datetime.datetime.strptime(responseModifiedTimeStr, '%a, %d %b %Y %H:%M:%S GMT').timestamp()
                
                haveLocalCopy = os.path.exists(imgDestination)
                if(haveLocalCopy):
                    localModifiedTime = os.path.getmtime(imgDestination)
                    if (localModifiedTime > responseModifiedTime):
                        if verboser:
                            print("passing on ", imgDestination)
                        continue

                if verboser:
                    print("downloading", imgDestination)

                file_name, headers = urllib.request.urlretrieve(imgSRC, imgDestination);
                num_new_downloaded += 1
                
                # Crop the image to a square shape if it is not already
                img = Image.open(imgDestination)
                w, h = img.size
                if w != h :
                    short_edge = w if w < h else h
                    img.crop((0, 0, short_edge, short_edge)).save(imgDestination)

    if(verbose):
        print("Downloaded", num_new_downloaded, "new files out of", num_total_imgs, "total images.")


## Main
usageString = """Usage:  python3 pull-data.py --production --primitives
   or:  python3 pull-data.py --articles --pictures
   etc.
Arguments:
    --production    output the data to the production versions of the json
                    files instead of the staging versions. Does not apply
                    to images, which are always considered "production"
    --primitives    update the primitive metadata from the google sheet
    --articles      update the articles metadata from the google sheet. 
    --videos        update the videos metadata from the google sheet 
    --pictures      download all the pictures from the models library site. 
                    Note that these *always* go to the production directory
                    and that for any image that we already have a copy of, 
                    we only download it if the remote one is newer. 
    -v, --verbose   verbose mode
    -vv, --verboser extremely verbose mode (python-print each entry as it is 
                    processed)
    --help          show this message
"""

if __name__ == "__main__":
    num_args = len(sys.argv) 
    arg_index = 1 ## the name of the python file coutns as an arg, so we start at 1
    if num_args == 1:
        print(usageString)
        sys.exit('Error: No arguments provided')
    
    while arg_index < num_args:
        arg = sys.argv[arg_index]
        if arg == "--help" or arg == "-help":
            print(usageString)
        elif arg == "-v" or arg == "--verbose":
            verbose = True
        elif arg == "-vv" or arg == "--verboser":
            verbose = True
            verboser = True
        elif arg == "--production":
            production = True
            output_path = PRODUCTION_JSON_PATH
        elif arg == "--primitives":
            outputtingPrimitives = True
        elif arg == "--articles":
            outputtingArticles = True
        elif arg == "--videos":
            outputtingVideos = True
        elif arg == "--pictures":
            outputtingPictures = True
        else:
            sys.exit("invalid argument: " + arg)

        arg_index += 1

    if(not outputtingPrimitives and not outputtingArticles and not outputtingVideos and not outputtingPictures):
        sys.exit('You did not specify any data sources to update. Try the "--help" option to see usage')

    ## see https://stackoverflow.com/a/1432949/6141684
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

    if outputtingPrimitives:
        populatePrimitives()
    if outputtingArticles:
        processArticles()
    if outputtingVideos:
        processVideos()
    if outputtingPictures:
        processPictures()
    sys.exit(0); ## 0 is unix for "all good"
