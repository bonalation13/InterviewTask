# this is Task1 of challenge 
# creating a python script to perform recursive operation of string substitution

    
import os
import sys

def replace_in_file(file_path, old_string, new_string):
    with open(file_path, 'r') as f:
        file_contents = f.read()

    file_contents = file_contents.replace(old_string, new_string)

    with open(file_path, 'w') as f:
        f.write(file_contents)

def replace_in_directory(directory_path, old_string, new_string):
    for dirpath, dirnames, filenames in os.walk(directory_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            replace_in_file(file_path, old_string, new_string)

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print('Usage: python script.py old_string new_string directory_path')
        sys.exit(1)

    old_string = sys.argv[1]
    new_string = sys.argv[2]
    directory_path = sys.argv[3]

    replace_in_directory(directory_path, old_string, new_string)

