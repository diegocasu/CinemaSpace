import pandas
import json

csvFilms = pandas.read_csv("movies_metadata.csv", low_memory= False)


def replace_string(productionString):
    work = productionString

    work = work.replace("'", '"')
    work = work.replace('Cote D"Ivoire',"Cote D'Ivoire" )
    work = work.replace('Lao People"s Democratic Republic',"Lao People's Democratic Republic")

    return work


for index in range(0, len(csvFilms["production_countries"])):
    productionString = csvFilms["production_countries"][index]

    if pandas.isnull(productionString):
        csvFilms["production_countries"][index] = "[]"
        continue

    if productionString == "[]":
        continue

    baseString = ""
    jsonString = replace_string(productionString)
    jsonStructure = json.loads(jsonString)

    for element in jsonStructure:
        baseString = baseString + '"' + element.pop("name") + '",'

    baseString = "[" + baseString[:-1] + "]"
    csvFilms["production_countries"][index] = baseString

csvFilms.to_csv("movies_metadata.csv", index=False)