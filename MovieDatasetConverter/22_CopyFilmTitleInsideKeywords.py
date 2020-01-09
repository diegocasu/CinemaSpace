import json
import time

start_time = time.time()

with open('Film.json', 'r', encoding='utf-8') as film_file, open('output.json', 'a', encoding='utf-8' ) as out_file:

    for line in film_file:
        film = json.loads(line)
        #print(film)

        filmTitle = film['title']
        film['keywords'].append(filmTitle)

        #print(filmTitle)
        #print(film['keywords'])

        newFilm = json.dumps(film)

        out_file.write(newFilm + '\n')

print("--- %s seconds ---" % (time.time() - start_time))