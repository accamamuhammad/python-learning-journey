# Writing files (.txt, .json, .csv)

import json
import csv

staff = [
    ['Name', 'Age', 'role'],
    ['luffy', 19, 'captain'],
    ['nami', 20, 'navigator'],
    ['zoro', 24, 'swordsman'],
    ['sanji', 22, 'cook']
]

employees = ['Luffy', 'Zoro', 'Sanjo', 'Nami']

employee = {
    'name': 'Luffy',
    'age': 19,
    'role': 'Captain'
}

file_path = 'crew.csv'

try:
    with open(file_path, 'w') as file:
        # TXT
        file.writelines(employees)
        # JSON
        json.dump(employee, file, indent=4)
        # CSV
        writer = csv.writer(file)
        for row in staff:
            writer.writerow(row)
        print(f'file {file_path} was created')
except FileExistsError:
    print('That file already exists')
