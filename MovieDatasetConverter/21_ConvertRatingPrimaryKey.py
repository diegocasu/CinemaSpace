import json
import time

start_time = time.time()

with open('Rating.json', 'r', encoding='utf-8') as rating_file, open('output.json', 'a', encoding='utf-8' ) as out_file:

    for line in rating_file:
        rating = json.loads(line)
        #print(rating)

        userId = rating.pop('userId')
        filmId = rating.pop('filmId')

        newPrimaryKey = '{' + "'userId': " + str(userId) + ', ' + "'filmId': " + str(filmId) + "}"
        rating['_id'] = newPrimaryKey

        newRating = json.dumps(rating)
        #print(newRating)
        newRating = newRating.replace("'", '"')
        newRating = newRating.replace('"{',"{")
        newRating = newRating.replace('}"', "}")
        #print(newRating)

        #json.loads(newRating)


        out_file.write(newRating + '\n')

print("--- %s seconds ---" % (time.time() - start_time))