import json
import csv
import urllib.request
import io

## staging file -- for checking 
# outputFile = "./staging.json"

## actual primitives file
outputFile = "../app/static/primitives.json"

## this is the value after the /d/ in the sharing url
## https://docs.google.com/spreadsheets/d/1h0sejFQ6ms5egYG0qJlWHU8Ep_rARZJrj86QRrMmaWI/edit?usp=sharing
sheetUID = "1h0sejFQ6ms5egYG0qJlWHU8Ep_rARZJrj86QRrMmaWI"
## found in the address bar when you select each page
pagesToPull = [0, 1561591207, 1474194526] ## James, Sydney, Nala

out = {"primitives" : {}}
primitives = out["primitives"]

for page in pagesToPull:
    ## make a http request and convert it into a string file object representation
    HTTPResponse = urllib.request.urlopen("https://docs.google.com/spreadsheets/d/" + sheetUID + "/export?format=csv&gid=" + str(page))
    csvBytes = io.BytesIO(HTTPResponse.read())
    csvfile = io.TextIOWrapper(csvBytes, encoding="utf-8")

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
            search_terms = [term.strip() for term in row[8].split(',')]
        
        agents = []
        if row[3] == "TRUE":
            agents.append("observer")
        if row[4] == "TRUE":
            agents.append("turtles")
        if row[5] == "TRUE":
            agents.append("patches")
        if row[6] == "TRUE":
            agents.append("links")
        if row[7] == "TRUE":
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

## dump to file
with open(outputFile, 'w') as outfile:
    json.dump(out, outfile, indent=4)

## print, if you want to
# print(json.dumps(out, indent=4))