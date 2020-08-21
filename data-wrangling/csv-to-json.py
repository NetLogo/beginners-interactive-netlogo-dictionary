import json
import csv

inputFile = "./small.csv"
outputFile = "./output.json"

out = {"primitives" : {}}
primitives = out["primitives"]

with open(inputFile, newline='') as csvfile:
    csvfile.readline() ## read the header line before parsing
    reader = csv.reader(csvfile, delimiter = ",", quotechar='"')
    for row in reader:
        name = row[0]
        
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
            "short_description" : short_description,
            "search_terms" : search_terms,
            "agents" : agents, 
            "see_also" : see_also,
            "library_models": library_models
        }

## dump to file
with open(outputFile, 'w') as outfile:
    json.dump(out, outfile, indent=4)

## print
print(json.dumps(out, indent=4))