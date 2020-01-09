import pandas

csvFilms = pandas.read_csv("movies_metadata.csv", low_memory= False)

del csvFilms['adult']
del csvFilms['belongs_to_collection']
del csvFilms['imdb_id']
del csvFilms['popularity']
del csvFilms['video']
del csvFilms['vote_average']
del csvFilms['vote_count']

csvFilms.to_csv("movies_metadata.csv", index=False)