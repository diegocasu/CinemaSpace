import re
import json


def replaceDoubleQuotesInsideArrays(match):
    newMatch = match.group(0).replace('\\"', '"')
    return newMatch

def replaceSquareWithRound(match):
    newMatch = match.group(0).replace('[', '(')
    newMatch = newMatch.replace(']', ')')
    return newMatch


with open('Film.json', 'r', encoding='utf-8') as file:
    file_lines = file.readlines()

    for index in range(0,len(file_lines)):
        file_lines[index] = file_lines[index].replace("[Cameo]", "(Cameo)")
        file_lines[index] = file_lines[index].replace("[cameo]", "(Cameo)")
        file_lines[index] = file_lines[index].replace("[Extra]", "(Extra)")
        file_lines[index] = file_lines[index].replace("[extra]", "(Extra)")
        file_lines[index] = file_lines[index].replace("[Singing voice]", "(Singing voice)")
        file_lines[index] = file_lines[index].replace("['Big Harry']", "('Big Harry')")
        file_lines[index] = file_lines[index].replace("[Krugli]", "(Krugli)")
        file_lines[index] = file_lines[index].replace("[bit]", "(bit)")
        file_lines[index] = file_lines[index].replace("[Script name: Moguera]", "(Script name: Moguera)")
        file_lines[index] = file_lines[index].replace("[ca]", "(ca)")
        file_lines[index] = file_lines[index].replace("[no 'Queen Grenda' in this film; thats just an IMDbism!]",
                                                      "(no 'Queen Grenda' in this film; thats just an IMDbism!)")
        file_lines[index] = file_lines[index].replace("[jp]", "(jp)")
        file_lines[index] = file_lines[index].replace("[english version]", "(english version)")
        file_lines[index] = file_lines[index].replace("[IMDb Name: Sgt. Bromley]", "(IMDb Name: Sgt. Bromley)")
        file_lines[index] = file_lines[index].replace("[voice: Cantonese]", "(voice: Cantonese)")
        file_lines[index] = file_lines[index].replace("[ph]", "(ph)")
        file_lines[index] = file_lines[index].replace("[fr]", "(fr)")
        file_lines[index] = file_lines[index].replace("[ve]", "(ve)")
        file_lines[index] = file_lines[index].replace("[intro]", "(intro)")
        file_lines[index] = file_lines[index].replace("[unconfirmed Cameo]", "(unconfirmed Cameo)")
        file_lines[index] = file_lines[index].replace("[new edit]", "(new edit)")
        file_lines[index] = file_lines[index].replace("[Mimino]", "(Mimino)")
        file_lines[index] = file_lines[index].replace("[Harper, in credits]", "(Harper, in credits)")
        file_lines[index] = file_lines[index].replace("[uncredited]", "(uncredited)")
        file_lines[index] = file_lines[index].replace("[himself]", "(himself)")
        file_lines[index] = file_lines[index].replace("[Vodyanoy]", "(Vodyanoy)")
        file_lines[index] = file_lines[index].replace("[Lucy's Friend]", "(Lucy's Friend)")
        file_lines[index] = file_lines[index].replace("[voice]", "(voice)")
        file_lines[index] = file_lines[index].replace("[Barr]", "(Barr)")
        file_lines[index] = file_lines[index].replace("[Good]", "(Good)")
        file_lines[index] = file_lines[index].replace("[Anidag]", "(Anidag)")
        file_lines[index] = file_lines[index].replace("[Abag]", "(Abag)")
        file_lines[index] = file_lines[index].replace("[Nushrok]", "(Nushrok)")
        file_lines[index] = file_lines[index].replace("[Jagupop 77]", "(Jagupop 77)")
        file_lines[index] = file_lines[index].replace("[Aunt Aksal]", "(Aunt Aksal)")
        file_lines[index] = file_lines[index].replace("[Grood]", "(Grood)")
        file_lines[index] = file_lines[index].replace("[Scenes deleted]", "(Scenes deleted)")
        file_lines[index] = file_lines[index].replace("[Atamansha]", "(Atamansha)")
        file_lines[index] = file_lines[index].replace("[Pyatachok]", "(Pyatachok)")
        file_lines[index] = file_lines[index].replace("[ピゴ]", "(ピゴ)")
        file_lines[index] = file_lines[index].replace("[ララ]", "(ララ)")
        file_lines[index] = file_lines[index].replace("[ペペ]", "(ペペ)")
        file_lines[index] = file_lines[index].replace("[ロロ]", "(ロロ)")
        file_lines[index] = file_lines[index].replace("[ニニ]", "(ニニ)")
        file_lines[index] = file_lines[index].replace("[トト]", "(トト)")
        file_lines[index] = file_lines[index].replace("[マック]", "(マック)")
        file_lines[index] = file_lines[index].replace("[ジャック]", "(ジャック)")
        file_lines[index] = file_lines[index].replace("[archival]", "(archival)")
        file_lines[index] = file_lines[index].replace("[Malysh]", "(Malysh)")
        file_lines[index] = file_lines[index].replace("[Judas Iscariot]", "(Judas Iscariot)")
        file_lines[index] = file_lines[index].replace("[2 Roles]", "(2 Roles)")
        file_lines[index] = file_lines[index].replace("[Unknown]", "(Unknown)")
        file_lines[index] = file_lines[index].replace("[Morozko]", "(Morozko)")
        file_lines[index] = file_lines[index].replace("[Varvara]", "(Varvara)")

        file_lines[index] = re.sub('\[Chs(.*?)\]', replaceSquareWithRound, file_lines[index])
        file_lines[index] = re.sub('\[Ch(.*?)\]', replaceSquareWithRound, file_lines[index])

        file_lines[index] = file_lines[index].replace('"[]"', '[]')
        file_lines[index] = file_lines[index].replace('"genres":"[', '"genres":[')
        file_lines[index] = file_lines[index].replace(']","homepage"', '],"homepage"')
        file_lines[index] = file_lines[index].replace('"production_companies":"[', '"production_companies":[')
        file_lines[index] = file_lines[index].replace(']","production_countries"', '],"production_countries"')
        file_lines[index] = file_lines[index].replace('"production_countries":"[', '"production_countries":[')
        file_lines[index] = file_lines[index].replace(']","release_date"', '],"release_date"')
        file_lines[index] = file_lines[index].replace('"spoken_languages":"[', '"spoken_languages":[')
        file_lines[index] = file_lines[index].replace(']","status"', '],"status"')
        file_lines[index] = file_lines[index].replace('"keywords":"[', '"keywords":[')
        file_lines[index] = file_lines[index].replace(']","cast"', '],"cast"')
        file_lines[index] = file_lines[index].replace('"cast":"[', '"cast":[')
        file_lines[index] = file_lines[index].replace(']","crew"', '],"crew"')
        file_lines[index] = file_lines[index].replace('"crew":"[', '"crew":[')
        file_lines[index] = file_lines[index].replace('}]"}', '}]}')

        file_lines[index] = re.sub('"genres":\[(.*?)\]', replaceDoubleQuotesInsideArrays, file_lines[index])
        file_lines[index] = re.sub('"cast":\[(.*?)\]', replaceDoubleQuotesInsideArrays, file_lines[index])
        file_lines[index] = re.sub('"crew":\[(.*?)\]', replaceDoubleQuotesInsideArrays, file_lines[index])
        file_lines[index] = re.sub('"keywords":\[(.*?)\]', replaceDoubleQuotesInsideArrays, file_lines[index])
        file_lines[index] = re.sub('"spoken_languages":\[(.*?)\]', replaceDoubleQuotesInsideArrays, file_lines[index])
        file_lines[index] = re.sub('"production_countries":\[(.*?)\]', replaceDoubleQuotesInsideArrays, file_lines[index])
        file_lines[index] = re.sub('"production_companies":\[(.*?)\]', replaceDoubleQuotesInsideArrays, file_lines[index])

        print(index)

with open('Film.json', 'w', encoding='utf-8') as file:
    file.writelines(file_lines)
