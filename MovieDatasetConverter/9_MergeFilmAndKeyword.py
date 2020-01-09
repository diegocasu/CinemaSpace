import pandas

csvKeywords = pandas.read_csv("keywords.csv", low_memory= False)
csvFilms = pandas.read_csv("movies_metadata.csv", low_memory= False)

mergedCsv = pandas.merge(left=csvFilms, right=csvKeywords, how='left', on='id')

for index in range(0, len(mergedCsv["keywords"])):
    if pandas.isnull(mergedCsv["keywords"][index]):
        mergedCsv["keywords"][index] = "[]"

mergedCsv.to_csv("movies_metadata.csv", index=False)