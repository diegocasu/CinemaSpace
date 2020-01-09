import pandas

csvUsers = pandas.read_csv("users.csv", low_memory=False)
csvRatings = pandas.read_csv("ratings.csv", low_memory=False)

mergedCsv = pandas.merge(left=csvRatings, right=csvUsers, how='left', left_on='userId', right_on="id")

print("start delete")

del mergedCsv['id']
del mergedCsv['administrator']
del mergedCsv['email']
del mergedCsv['password']
del mergedCsv['username']
del mergedCsv['date_of_birth']

print("end delete")

mergedCsv.to_csv("ratings.csv", index=False)
