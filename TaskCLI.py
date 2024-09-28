import os
import sys
import json

#print("Script name:", sys.argv[0])  # This is the script name
#print("Arguments:", sys.argv[1:])  

#First check to see if the file exists/and not null
#Read json object and convert to 

file_path = 'tasks.json'
jObject = ''
# check for file path

##TURN THIS INTO A FUNCTION AND CALL IT IT IN EACH COMMAND
##WHEN NEEDED.
## Function will need to return a string
if os.path.isfile(file_path) and os.path.getsize(file_path) > 0: 
   print("Welcome back") 
   with open(file_path, 'r') as file:
        content = file.read()
        tasks = json.loads(content)

num_tasks = len(jObject)
    

if sys.argv[1] == 'add' and sys.argv[2] and len(sys.argv[]) == 3:
    num_tasks += 1
    tasks[num_tasks] = sys.argv[2]
    print("Task added successfully")

# elif sys.argv[1] == 'update':
#     print('')
# elif sys.argv[1] == 'delete':
#     print('')
# elif sys.argv[1] == 'mark-in-progress':
#     print('')
# elif sys.argv[1] == 'list':
#     print('')    

def check_for_file(): #check this before all commands
    pass

def delete_file(): #only trigger if 1 item on file and it gets deleted
    pass

def create_file(): #if no file exists - Add only
    pass
#will only run if exists. Will probably be nested 
#into check for file
def read_file(): 
    pass
