import json
import time


def createObjectIdDictionary(film_file):
    obj_dict = dict()

    for film_line in film_file:
        film = json.loads(film_line)
        newKey = str(film['id'])
        newValue = film["_id"]
        obj_dict[newKey] = newValue

    return obj_dict


start_time = time.time()

with open('Rating.json', 'r', encoding='utf-8') as rating_file, open('Film.json', 'r', encoding='utf-8') as film_file, open('output.json', 'a', encoding='utf-8' ) as out_file:
    objectIdDictionary = createObjectIdDictionary(film_file)
    counterRating = 0

    print("--- %s seconds ---" % (time.time() - start_time))

    for line in rating_file:
        rating = json.loads(line)
        #print(rating)

        filmId = rating['movieId']
        filmIdKey = str(filmId)

        if filmIdKey in objectIdDictionary:
            counterRating = counterRating + 1

            objectId = objectIdDictionary[filmIdKey]
            rating.pop('movieId')
            rating['filmId'] = objectId

            newRating = json.dumps(rating)
            #print(newRating)
            #print("********")
            
            out_file.write(newRating + '\n')
        else:
            #print("Non trovato")
            #print(filmIdKey)
            continue

print(counterRating)
print("--- %s seconds ---" % (time.time() - start_time))