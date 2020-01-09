import pandas
import numpy


csvRatings = pandas.read_csv("ratings.csv", low_memory= False)

print("loaded")

csvRatings.insert(len(csvRatings.columns), "age_of_user", 0);
csvRatings["age_of_user"] = numpy.random.randint(16, 55, size=len(csvRatings))

print("modified")

csvRatings.to_csv("ratings.csv", index=False)


