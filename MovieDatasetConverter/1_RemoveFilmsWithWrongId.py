import pandas

csvFilms = pandas.read_csv("movies_metadata.csv", low_memory= False)

csvFilms.drop(csvFilms[ csvFilms["id"] == "1997-08-20"].index, inplace=True)
csvFilms.drop(csvFilms[ csvFilms["id"] == "2012-09-29"].index, inplace=True)
csvFilms.drop(csvFilms[ csvFilms["id"] == "2014-01-01"].index, inplace=True)

csvFilms.to_csv("movies_metadata.csv", index=False)