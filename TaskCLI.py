import os
import argparse

file_path = 'tasks.json'
# check for file path
if os.path.isfile(file_path): 
    print("Welcome back")
else: 
    with open(file_path, 'w') as file:
        #file.write