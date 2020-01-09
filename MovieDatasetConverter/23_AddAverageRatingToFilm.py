import json
import time


def createFilmAverageRatingDictionary(rating_file):
    sum_of_rating_dict = dict()
    num_of_rating_dict = dict()

    for rating_line in rating_file:
        rating = json.loads(rating_line)
        film_id = str(rating['_id']['filmId'])

        if film_id in sum_of_rating_dict:
            sum_of_rating_dict[film_id] += rating['rating']
            num_of_rating_dict[film_id] += 1
        else:
            sum_of_rating_dict[film_id] = rating['rating']
            num_of_rating_dict[film_id] = 1

    return sum_of_rating_dict, num_of_rating_dict


start_time = time.time()

with open('Rating.json', 'r', encoding='utf-8') as rating_file, open('Film.json', 'r', encoding='utf-8') as film_file, open('output.json', 'a', encoding='utf-8' ) as out_file:
    sum_of_ratings, num_of_ratings = createFilmAverageRatingDictionary(rating_file)

    for film_line in film_file:
        film = json.loads(film_line)
        filmId = str(film['_id'])

        if filmId in sum_of_ratings:
            film_avg = sum_of_ratings[filmId] / num_of_ratings[filmId]
            film_numberOfRatings = num_of_ratings[filmId]
        else:
            film_avg = 0
            film_numberOfRatings = 0

        film['average_rating'] = film_avg
        film['number_of_ratings'] = film_numberOfRatings

        newFilm = json.dumps(film)

        out_file.write(newFilm + '\n')

print("--- %s seconds ---" % (time.time() - start_time))