import pandas
import json

csvFilms = pandas.read_csv("movies_metadata.csv", low_memory= False)


def replace_string(languagesString):
    work = languagesString

    work = work.replace("'", '"')
    work = work.replace("\\","")

    return work


for index in range(0, len(csvFilms["spoken_languages"])):
    languagesString = csvFilms["spoken_languages"][index]

    if pandas.isnull(languagesString):
        csvFilms["spoken_languages"][index] = "[]"
        continue

    if languagesString == "[]":
        continue

    baseString = ""
    jsonString = replace_string(languagesString)
    jsonStructure = json.loads(jsonString)

    for element in jsonStructure:
        baseString = baseString + '"' + element.pop("name") + '",'

    baseString = "[" + baseString[:-1] + "]"
    csvFilms["spoken_languages"][index] = baseString

csvFilms.to_csv("movies_metadata.csv", index=False)