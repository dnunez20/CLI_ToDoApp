import os
import sys
import json


#check that input is valid. If none are true then program will exit and avoid read/write
add = True if sys.argv[1] == 'add' and len(sys.argv) == 3 else False
update = True if sys.argv[1] == 'update' and len(sys.argv) == 4 else False
delete = True if sys.argv[1] == 'delete' and len(sys.argv) == 3 else False

if not (add or update or delete):
    sys.exit()

file_path = 'tasks.json'
tasks = None

#First check to see if the file exists/and not null
#Read json object and convert to dictionary
if os.path.isfile(file_path) and os.path.getsize(file_path) > 0: 
   with open(file_path, 'r') as file:
        content = file.read()
        tasks = json.loads(content)

if add: 
    if tasks:
    
    else:
    file = open('tasks.json', 'w')
    arr = {1 : sys.argv[2] }

#num_tasks = len(tasks)

    

# if add:
#     num_tasks += 1
#     tasks[num_tasks] = sys.argv[2]
#     print("Task added successfully")
#     #TODO Write to file
#     else: 
#         file = 
#         tasks.json
# elif sys.argv[1] == 'update':
#     print('')
# elif sys.argv[1] == 'delete':
#     print('')
# # elif sys.argv[1] == 'mark-in-progress':
# #     print('')
# # elif sys.argv[1] == 'list':
# #     print('')    

# def check_for_file(): #check this before all commands
#     pass

# def delete_file(): #only trigger if 1 item on file and it gets deleted
#     pass

# def create_file(): #if no file exists - Add only
#     pass
# #will only run if exists. Will probably be nested 
# #into check for file
# def read_file(): 
#     pass
