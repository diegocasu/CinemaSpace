import pandas

csvCredits = pandas.read_csv("credits.csv", low_memory= False)
csvFilms = pandas.read_csv("movies_metadata.csv", low_memory= False)

mergedCsv = pandas.merge(left=csvFilms, right=csvCredits, how='left', on='id')

for index in range(0, len(mergedCsv["cast"])):
    if pandas.isnull(mergedCsv["cast"][index]):
        mergedCsv["cast"][index] = "[]"

for index in range(0, len(mergedCsv["crew"])):
    if pandas.isnull(mergedCsv["crew"][index]):
        mergedCsv["crew"][index] = "[]"

mergedCsv.to_csv("movies_metadata.csv", index=False)