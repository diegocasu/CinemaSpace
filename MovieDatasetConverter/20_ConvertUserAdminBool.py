
with open('User.json', 'r', encoding='utf-8') as user_file:
    file_lines = user_file.readlines()

    for index in range(0,len(file_lines)):
        file_lines[index] = file_lines[index].replace('"administrator":0','"administrator":false')
        file_lines[index] = file_lines[index].replace('"administrator":1', '"administrator":true')

with open('User.json', 'w', encoding='utf-8') as user_file:
        user_file.writelines(file_lines)