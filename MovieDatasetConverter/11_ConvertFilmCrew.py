import pandas
import json
import re

def replaceInnerStringSingleQuotes(match):
    newMatch = match.group(0).replace("'",'"')
    return newMatch

def replaceInnerStringDoubleQuotes(match):
    newMatch = match.group(0).replace('"',"'")
    return newMatch

def replace_string(crewString):
    work = crewString

    work = work.replace("'department'", '"department"')
    work = work.replace("'job'", '"job"')
    work = work.replace("'credit_id'", '"credit_id"')
    work = work.replace("'gender'", '"gender"')
    work = work.replace("'id'", '"id"')
    work = work.replace("'name'", '"name"')
    work = work.replace("'profile_path'", '"profile_path"')

    work = work.replace('"profile_path": \'','"profile_path": "')
    work = work.replace("'},",'"},')
    work = work.replace("'}]", '"}]')

    work = work.replace(": None", ': ""')

    work = re.sub("\s'(.*?)',", replaceInnerStringSingleQuotes, work)
    work = re.sub('[A-Za-z]\s"(.*?)"\s[A-Za-z]', replaceInnerStringDoubleQuotes, work)
    work = re.sub('[A-Za-z\.]\s"(.*?)"\s[A-Za-z]', replaceInnerStringDoubleQuotes, work)

    work = work.replace('"Randy "Fife""', '"Randy \'Fife\'"')
    work = work.replace('""Weird Al"', '"\'Weird Al\'')
    work = work.replace('"Bryan "the brain"  Mantia"', '"Bryan \'the brain\' Mantia"')
    work = work.replace('"Edvard van "t Wout"', '"Edvard van \'t Wout\'"')
    work = work.replace('"José "Pepe" Ojeda"', '"José \'Pepe\' Ojeda"')

    return work


csvCredits = pandas.read_csv("credits.csv", low_memory= False)

for index in range(0, len(csvCredits["crew"])):
    crewString = csvCredits["crew"][index]

    if pandas.isnull(crewString):
        crewString["crew"][index] = "[]"
        continue

    if crewString == "[]":
        continue

    baseString = ""
    jsonString = replace_string(crewString)
    jsonStructure = json.loads(jsonString)

    for json_index in range(0, len(jsonStructure)):
        baseString = baseString + '{' + '"department" : "' + jsonStructure[json_index].pop("department") + '", '
        baseString = baseString + '"job" : "' + jsonStructure[json_index].pop("job") + '", '
        baseString = baseString + '"name": "' + str(jsonStructure[json_index].pop("name")) + '", '
        baseString = baseString + '"profile_path": "' + jsonStructure[json_index].pop("profile_path") + '"' + '}, '

    baseString = "[" + baseString[:-2] + "]"
    csvCredits["crew"][index] = baseString

csvCredits.to_csv("credits.csv", index=False)