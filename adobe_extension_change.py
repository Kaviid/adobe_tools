
import re
from pathlib import Path

#Get User extension which user need to change
def correct_format () :
    user_format = input('Which extension u need to convert : ').lower().strip()
    if user_format == 'ai':
        return '.ai'
    elif user_format == 'eps':
        return '.eps'
    elif user_format == 'svg':
        return '.svg'
    else:
        print('Usage <1, 2, 3 | ai, eps, svg>')

#Store orginal csv data
def Get_metadata (path) :
    with open(path, 'r') as file:
        content = file.readlines()
    return content

#Replace orginal one to we want version
def replace_format (ext_name,content,path):
    updated = [] #Collect changed each files
    for line in content:
        m = re.sub(r'\.([a-zA-Z0-9]+)', ext_name , line)
        updated.append(m)

    with open (path, 'w') as file : #Change orginal file
        for i in updated:
            if i.strip(): #Ignore if have any blank or empty lines
                file.write(i)

user_file_name =  input('Enter file name : ')
path = Path(__file__).parent.resolve() / user_file_name

replace_format( 
    correct_format() , 
    Get_metadata (path),
    path
    )

