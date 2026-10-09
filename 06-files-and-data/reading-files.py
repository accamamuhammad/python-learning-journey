# Python read files (.txt, .json, .csv)

import json
import csv

file_path = 'output.json'

try:
    with open(file_path, 'r') as file:
        # TXT
        content = file.read()
        print(content)

except FileExistsError:
    print('File already exists')
except FileNotFoundError:
    print('File not found')
except PermissionError:
    print('You dont have permission to read that file')
