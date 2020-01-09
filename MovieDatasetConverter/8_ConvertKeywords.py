import pandas
import json

csvKeywords = pandas.read_csv("keywords.csv", low_memory= False)


def replace_string(keywordsString):
    work = keywordsString

    work = work.replace("'id'", '"id"')
    work = work.replace("'name': '",'"name": "')
    work = work.replace("'}", '"}')
    work = work.replace("'name'",'"name"')
    work = work.replace("\\", "")
    work = work.replace('"trudy jackson"', "trudy jackson")

    return work


for index in range(0, len(csvKeywords["keywords"])):
    keywordsString = csvKeywords["keywords"][index]

    if pandas.isnull(keywordsString):
        csvKeywords["keywords"][index] = "[]"
        continue

    if keywordsString == "[]":
        continue

    baseString = ""
    jsonString = replace_string(keywordsString)
    jsonStructure = json.loads(jsonString)

    for element in jsonStructure:
        baseString = baseString + '"' + element.pop("name") + '",'

    baseString = "[" + baseString[:-1] + "]"
    csvKeywords["keywords"][index] = baseString

csvKeywords.to_csv("keywords.csv", index=False)