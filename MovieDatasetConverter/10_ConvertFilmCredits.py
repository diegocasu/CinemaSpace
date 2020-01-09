import pandas
import json
import re


def replaceInnerStringDoubleQuotes(match):
    newMatch = match.group(0).replace('"',"'")
    return newMatch

def replaceInnerStringQuoteApostrophe(match):
    newMatch = match.group(0).replace('"',"'")
    newMatch = newMatch.replace('“', "'")
    return newMatch

def replaceDoubleQuotesInternalOnly(match):
    newMatch = match.group(0).replace('"',"'")
    newString = newMatch[0] + '"' + newMatch[2:-3] + '"' + newMatch[-1]
    return newString

def replaceInnerDoubleQuoteExceptBeginning(match):
    newMatch = match.group(0).replace('"',"'")
    newString = '"' + newMatch[1:-1]
    return newString

def replace_string(creditsString):
    work = creditsString

    work = re.sub('\s"(.*?)"\s', replaceInnerStringDoubleQuotes, work)
    work = re.sub('\s"(.*?)"\)', replaceInnerStringDoubleQuotes, work)
    work = re.sub('\s"(.*?)“', replaceInnerStringQuoteApostrophe, work)
    work = re.sub('\("(.*?)"\)', replaceInnerStringDoubleQuotes, work)
    work = re.sub('\s"(.*?)"', replaceInnerStringDoubleQuotes, work)
    work = re.sub('"(.*?)"\s', replaceInnerStringDoubleQuotes, work)

    work = work.replace("'cast_id'", '"cast_id"')
    work = work.replace("'character'", '"character"')
    work = work.replace("'credit_id'", '"credit_id"')
    work = work.replace("'gender'", '"gender"')
    work = work.replace("'id'", '"id"')
    work = work.replace("'name'", '"name"')
    work = work.replace("'order'", '"order"')
    work = work.replace("'profile_path'", '"profile_path"')
    work = work.replace("'name'", '"name"')

    work = work.replace(": '", ': "')
    work = work.replace("', ", '", ')
    work = work.replace("'}", '"}')
    work = work.replace(": None", ': ""')
    work = work.replace('"Jack Jones"', 'Jack Jones')
    work = work.replace("Mark \\'Dags\" D\\'Agastino","Mark 'Dags' D'Agastino")
    work = work.replace('"The Whale"',"'The Whale'")
    work = work.replace('"Connie Doyle/"Patricia Winterbourne"', '"Connie Doyle/Patricia Winterbourne')
    work = work.replace("\\'","")
    work = work.replace('""German""','"German"')
    work = work.replace('Arthur \'Fine Art", a hustler',"Arthur 'Fine Art', a hustler")
    work = work.replace('\'Rocky"', "'Rocky'")
    work = work.replace("'Damian\",", "'Damian',")
    work = work.replace("'Pops\",", "'Pops',")
    work = work.replace('""Old Man""',"\"'Old Man'\"")
    work = work.replace('""Myth""', "\"'Myth'\"")
    work = work.replace('"character": ""Monsieur", le patron du bar à entraîneuses"', '"character": "\'Monsieur\', le patron du bar à entraîneuses"')

    ##################

    work = work.replace('"character": "", "','"character": stringAvoid, "')
    work = work.replace('"cast_id": "", "', '"cast_id": stringAvoid, "')
    work = work.replace('"credit_id": "", "', '"credit_id": stringAvoid, "')
    work = work.replace('"gender": "", "', '"gender": stringAvoid, "')
    work = work.replace('"id": "", "', '"id": stringAvoid, "')
    work = work.replace('"name": "", "', '"name": stringAvoid, "')
    work = work.replace('"order": "", "', '"order": stringAvoid, "')

    work = re.sub('\s""(.*?)"",', replaceDoubleQuotesInternalOnly, work)

    work = work.replace('"character": stringAvoid, "','"character": "", "',)
    work = work.replace('"cast_id": stringAvoid, "', '"cast_id": "", "', )
    work = work.replace('"credit_id": stringAvoid, "', '"credit_id": "", "', )
    work = work.replace('"gender": stringAvoid, "', '"gender": "", "', )
    work = work.replace('"id": stringAvoid, "', '"id": "", "', )
    work = work.replace('"name": stringAvoid, "', '"name": "", "', )
    work = work.replace('"order": stringAvoid, "', '"order": "", "', )

    ############################

    work = work.replace("'Ronny\"", "'Ronny'")
    work = work.replace("\"The Jewish Question'", "'The Jewish Question'")
    work = work.replace('"Thurman Merman The Kid""', '"Thurman Merman The Kid"')
    work = work.replace('O"Neal', "O'Neal")
    work = work.replace("'Korab\",", "'Korab',")
    work = work.replace("'Mądry\",", "'Mądry',")

    work = re.sub('\s' + "'" + '(.*?)", [a-z]', replaceInnerStringDoubleQuotes, work)
    work = re.sub('\s' + "'" + '(.*?)", [A-Z]', replaceInnerStringDoubleQuotes, work)

    work = re.sub('"' + "'" + '(.*?)", [A-Z]', replaceInnerDoubleQuoteExceptBeginning, work)
    work = re.sub('"' + "'" + '(.*?)", [a-z]', replaceInnerDoubleQuoteExceptBeginning, work)

    work = re.sub('\s' + "'" + '(.*?)", ' + "'", replaceInnerStringDoubleQuotes, work)
    work = re.sub('\s' + "'" + '(.*?)", ' + "&", replaceInnerStringDoubleQuotes, work)

    work = work.replace(": Jack Jones, ", ': "Jack Jones", ')
    work = work.replace(": 'The Whale',", ': "The Whale",')
    work = work.replace('Bauers/"Not Sure"', "Bauers/Not Sure")
    work = work.replace('No. 326"', "No. 326")
    work = work.replace("\\xad", "")
    work = work.replace("\\xa0", "")
    work = work.replace("\\x92s", "")
    work = work.replace('""Charlie"', '"Charlie')
    work = work.replace('E.J."Space"Hanlon', "E.J.'Space' Hanlon")
    work = work.replace('"Coward""', '"Coward"')
    work = work.replace(' Dill" ', ' Dill ')
    work = work.replace('""Candy Darling"', '"Candy Darling')
    work = work.replace('l"Americano"', "l'Americano'")
    work = work.replace('2O Straniero"','O Straniero')
    work = work.replace('""Жжёный"', '"Жжёный')
    work = work.replace('""Bum"(Vidyas mother)"','"Bum(Vidyas mother)"')
    work = work.replace('"Marauder Leader (segment \' M is for Marauder")"','"Marauder Leader (segment \'M is for Marauder\')"')
    work = work.replace('"Marauder Extras (segment \' M is for Marauder")"','"Marauder Extras (segment \'M is for Marauder\')"')
    work = work.replace('"Mom (segment: "The Visitant\')"','"Mom (segment: \'The Visitant\')"')
    work = work.replace(' "The Visitant\''," 'The Visitant'")
    work = work.replace(' "The Body\'', " 'The Body'")
    work = work.replace(' "Undying Love\'', " 'Undying Love'")
    work = work.replace(' "The Sleeping Plot\'', " 'The Sleeping Plot'")
    work = work.replace(' "Banishing\'', " 'Banishing'")
    work = work.replace(' "Death Scenes\'', " 'Death Scenes'")
    work = work.replace(' "Evaded\'', " 'Evaded'")
    work = work.replace('"Herself - Author: "The Madam Curie Complex\'"', "\"Herself - Author: 'The Madam Curie Complex'\"")
    work = work.replace('""Major"', '"Major')
    work = work.replace('"Himself: "Mr. Steadicam\'"',"\"Himself: 'Mr. Steadicam'\"")
    work = work.replace('""Malutki"', '"Malutki')

    return work


csvCredits = pandas.read_csv("credits.csv", low_memory= False)

for index in range(0, len(csvCredits["cast"])):
    creditsString = csvCredits["cast"][index]

    if pandas.isnull(creditsString):
        creditsString["cast"][index] = "[]"
        continue

    if creditsString == "[]":
        continue

    baseString = ""
    jsonString = replace_string(creditsString)
    jsonStructure = json.loads(jsonString)

    for json_index in range(0, len(jsonStructure)):
        jsonStructure[json_index].pop("cast_id")
        jsonStructure[json_index].pop("credit_id")
        jsonStructure[json_index].pop("gender")

        baseString = baseString + '{' + '"character" : "' + jsonStructure[json_index].pop("character") + '", '
        baseString = baseString + '"name" : "' + jsonStructure[json_index].pop("name") + '", '
        baseString = baseString + '"order": ' + str(jsonStructure[json_index].pop("order")) + ', '
        baseString = baseString + '"profile_path": "' + jsonStructure[json_index].pop("profile_path") + '"' + '}, '

    baseString = "[" + baseString[:-2] + "]"
    csvCredits["cast"][index] = baseString


csvCredits.to_csv("credits.csv", index=False)