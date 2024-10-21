import os
import sys
import json


#check that input is valid. If none are true then program will exit and avoid read/write
print(sys.argv)

if sys.argv[1] == 'add':
    add = True

file_path = 'tasks.json'

if add:
    print("WORKING")
    tasks = {
        "1" : sys.argv[2]
    }
    with open(file_path, 'w') as json_file:
        json.dump(tasks, json_file, indent=4)


# #Read json object and convert to dictionary
# if os.path.isfile(file_path) and os.path.getsize(file_path) > 0:
#    with open(file_path, 'r') as file:
#         content = file.read()
#         tasks = json.loads(content)

