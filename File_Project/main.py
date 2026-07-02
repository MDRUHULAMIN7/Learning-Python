from pathlib import Path


def readfileandfolder():    
     path = Path("")
     items = list(path.rglob('*'))
     for i, items in enumerate(items):
          print(f"{i+1} : {items } ")

def createfile():
    try:
         readfileandfolder()
         name = input("please enter your file name:- ")
         p = Path(name)
         if not p.exists():
            with open(p,"w") as fs:
                data = input("please enter your data:- ")
                fs.write(data)
            print("file created successfully")    
         else:
            print("file already exists")
    
    except Exception as err:
          print(f"there is an error: {err}")


def readfile():
    
    try:
        readfileandfolder()
        name = input("which file you want read:- ")
        p = Path(name)
        if p.exists() and p.is_file():
            with open(p,"r") as fs:
                data = fs.read()
                print(data)

            print("file read successfully")    
        else:
            print("file not found")
    except Exception as err:
         print(f"there is an error: {err}")


def updatefile():
    try:
        readfileandfolder()
        name = input("which file you want update:- ")
        p = Path(name)
        if p.exists() and p.is_file():
            print("press 1 for append data to file:- ")
            print("press 2 for overwrite data to file:- ")
            print("press 3 for appending some content in your file:- ")

            res = int(input("please tell your response:- "))

            if res == 1:
                name2 = input("tell your new file name:- ")
                p2 = Path(name2)
                p.rename(p2)

            if res == 2:
                with open(p,"w") as fs:
                    data = input("tell what you want to write this is overwrite the file:- ")
                    fs.write(data)

            if res == 3:
                with open(p,"a") as fs:
                    data = input("tell what you want to write this is append the file:- ")
                    fs.write(" " + data)

    except Exception  as err:
            print(f"there is an error: {err}")       




def deletefile():
    try:
        readfileandfolder()
        name = input("which file you want delete:- ")
        p = Path(name)
        if p.exists() and p.is_file():
            p.unlink()
            print("file deleted successfully")
        else:
            print("file not found")
    except Exception as err:
        print(f"there is an error: {err}")



print("press 1 for create a file")
print("press 2 for read a file")
print("press 3 for update to a file")
print("press 4 for delete a file")

check = int(input("please tell your response:- "))

if check == 1:
    createfile()

if check == 2:
    readfile()

if check == 3:
    updatefile()

if check == 4:
    deletefile()