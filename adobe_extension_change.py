
import re
from pathlib import Path
import sys

#Get User extension which user need to change
def correct_format () :
    user_format = input('Which extension u need to convert : ').lower().strip()
    if user_format in ('ai', 'eps', 'svg'):
        return f'.{user_format}'
    print('Usage: <ai, eps, svg>')
    sys.exit(1)

#Store orginal csv data
def Get_metadata (path) :
    try :
        with open(path, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"Error: file '{path.name}' not found.")
        sys.exit(1)

#Replace orginal one to we want version
def replace_format (ext_name,content,path):
    updated = [] #Collect changed each files
    for line in content:
        splited_line = line.split(',') #Checked untill here : DONE
        m = re.sub(r'\.([a-zA-Z0-9]+)', ext_name , splited_line[0])
        splited_line[0] = m
        joined_again = ",".join(splited_line)
        updated.append(joined_again)

    with open (path, 'w') as file : #Change orginal file
        for i in updated:
            if i.strip(): #Ignore if have any blank or empty lines
                file.write(i)

if __name__ == "__main__":
    user_file_name =  input('Enter file name : ')
    path = Path(__file__).parent.resolve() / user_file_name #Get path
    replace_format(correct_format() , Get_metadata (path), path)
