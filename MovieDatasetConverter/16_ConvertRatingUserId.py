import json
import time


def createObjectIdDictionary(user_file):
    obj_dict = dict()

    for user_line in user_file:
        user = json.loads(user_line)
        newKey = str(user['id'])
        newValue = user["_id"]
        obj_dict[newKey] = newValue

    return obj_dict


start_time = time.time()

with open('Rating.json', 'r', encoding='utf-8') as rating_file, open('User.json', 'r', encoding='utf-8') as user_file, open('output.json', 'a', encoding='utf-8' ) as out_file:
    objectIdDictionary = createObjectIdDictionary(user_file)

    print("--- %s seconds ---" % (time.time() - start_time))

    for line in rating_file:
        rating = json.loads(line)
        #print(rating)

        userId = rating['userId']
        objectId = objectIdDictionary[str(userId)]
        rating['userId'] = objectId

        #print(rating)

        newRating = json.dumps(rating)
        #print(newRating)

        #print("********")

        out_file.write(newRating + '\n')

print("--- %s seconds ---" % (time.time() - start_time))