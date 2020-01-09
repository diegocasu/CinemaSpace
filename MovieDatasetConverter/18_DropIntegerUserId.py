import json
import time

start_time = time.time()

with open('User.json', 'r', encoding='utf-8') as user_file, open('output.json', 'a', encoding='utf-8' ) as out_file:
    for line in user_file:
        user = json.loads(line)
        #print(user)

        user.pop('id')
        newUser = json.dumps(user)
        #print(newUser)
        #print("********")

        out_file.write(newUser + '\n')

print("--- %s seconds ---" % (time.time() - start_time))