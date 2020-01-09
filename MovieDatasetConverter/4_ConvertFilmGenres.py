import pandas
import json

csvFilms = pandas.read_csv("movies_metadata.csv", low_memory= False)

for index in range(0, len(csvFilms["genres"])):
    genreString = csvFilms["genres"][index];

    if genreString == "[]":
        continue

    baseString = ""
    x = genreString.replace("'", '"')
    jsonStructure = json.loads(x)
    for element in jsonStructure:
        element.pop("id")
        baseString = baseString + '"' + element.pop("name") + '",'

    baseString = "[" + baseString[:-1] + "]"
    csvFilms["genres"][index] = baseString;

csvFilms.to_csv("movies_metadata.csv", index=False)