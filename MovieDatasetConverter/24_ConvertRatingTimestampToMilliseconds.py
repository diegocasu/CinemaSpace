import json
import time

start_time = time.time()

with open('Rating.json', 'r', encoding='utf-8') as rating_file, open('output.json', 'a', encoding='utf-8' ) as out_file:
    for rating_line in rating_file:
        rating = json.loads(rating_line)
        rating['timestamp'] *= 1000
        newRating = json.dumps(rating)

        out_file.write(newRating + '\n')

print("--- %s seconds ---" % (time.time() - start_time))