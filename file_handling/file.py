### File handling in Python

from pathlib import Path

def readfileandfolder():
    path = Path('')
    items = list(path.rglob('*'))
    for i, item in enumerate(items):
        print(f"{i+1} : {item}")


def createfile():
    try:
        readfileandfolder()
        name = input("please tell your file name :- ")
        p = Path(name)
        if not p.exists() and p.is_file():
            with open(p,"w") as fs:
                data = input("what  you want to write in this file")
                fs.write(data)

            print(f"File created Successfully")        
        else:
            print("This file already exist")
    except Exception as err:
        print(f"An error occured,{err}")


def readfile():
    try:
        readfileandfolder() 
        name = input("which file you want to read")
        p = Path(name)
        if p.exists() and p.is_file():
            with open(p,'r') as fs:
                data = fs.read()
                print(data)
            
            print("Readed Successfully")

        else:
            print('the file dosenot exist')
    except Exception as err:
        print(f"An error occured {err}")
    





print('press 1 for creating a file ')
print('press 2 for reading a file ')
print('press 3 for updating a file ')
print('press 4 for deletion a file ')

check = int(input("please tell your response :- "))

if check == 1:
    createfile()

if check ==  2:
    readfile()

