# Python file detection

import os

file_path = 'test.txt'
file_path_2 = 'stuff/box.txt'

if os.path.exists(file_path_2):
    print(f"The location '{file_path_2}' exists")

    if os.path.isfile(file_path_2):
        print('That is a file')
else:
    print(f"The location '{file_path_2}' does not exist")
