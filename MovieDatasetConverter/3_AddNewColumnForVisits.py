import numpy
import pandas

csvFilms = pandas.read_csv("movies_metadata.csv", low_memory= False)

csvFilms.insert(len(csvFilms.columns), "number_of_visits", 0);
csvFilms["number_of_visits"] = numpy.random.randint(0,100000, size=len(csvFilms))

csvFilms.to_csv("movies_metadata.csv", index=False)