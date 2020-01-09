import pandas
import json


def replace_string(productionString):
    work = productionString

    work = work.replace("'name': '", '"name": "')
    work = work.replace("', 'id'", '", "id"')
    work = work.replace("'name'", '"name"')
    work = work.replace("'id'", '"id"')
    work = work.replace('"Tor"', 'Tor')
    work = work.replace('"A"', 'A')
    work = work.replace('"X"', 'X')
    work = work.replace('"Perspektywa"', 'Perspektywa')
    work = work.replace('"Kadr"', 'Kadr')
    work = work.replace("Perspektywa,", 'Perspektywa",')
    work = work.replace('"DIA"', 'DIA')
    work = work.replace('"Johannisthal"', 'Johannisthal')
    work = work.replace('"Kamera"', 'Kamera')
    work = work.replace('"Zespol Filmowy"', 'Zespol Filmowy')
    work = work.replace('"Pryzmat"', 'Pryzmat')
    work = work.replace('"Silesia"', 'Silesia')
    work = work.replace('"Oko"', 'Oko')
    work = work.replace('"Plan"', 'Plan')
    work = work.replace('"Syrena"', 'Syrena')
    work = work.replace(' Filmowy "', ' Filmowy ')
    work = work.replace('""', '"')
    work = work.replace(" Zespol Filmowy,",' "Zespol Filmowy", ')
    work = work.replace('"Das Kleine Fernsehspiel"', 'Das Kleine Fernsehspiel"')
    work = work.replace('"Tvorcheskoye Obyeduneniniye "Luch"', '"Tvorcheskoye Obyeduneniniye Luch"')
    work = work.replace('\\', "")
    work = work.replace('"Weltfilm"', 'Weltfilm')
    work = work.replace('"Orlenok"', 'Orlenok')
    work = work.replace('"Tsar"', 'Tsar"')
    work = work.replace('"Kvadrat"', 'Kvadrat"')
    work = work.replace('"Przedsiebiorstwo Realizacji Filmów "Zespoly Filmowe"', '"Przedsiebiorstwo Realizacji Filmów Zespoly Filmowe"')
    work = work.replace('"F.A.F"', 'F.A.F"')

    return work


csvFilms = pandas.read_csv("movies_metadata.csv", low_memory= False)

for index in range(0, len(csvFilms["production_companies"])):
    productionString = csvFilms["production_companies"][index]

    if pandas.isnull(productionString):
        csvFilms["production_companies"][index] = "[]"
        continue

    if productionString == "[]":
        continue

    baseString = ""
    jsonString = replace_string(productionString)
    jsonStructure = json.loads(jsonString)

    for element in jsonStructure:
        element.pop("id")
        baseString = baseString + '"' + element.pop("name") + '",'

    baseString = "[" + baseString[:-1] + "]"
    csvFilms["production_companies"][index] = baseString


csvFilms.to_csv("movies_metadata.csv", index=False)