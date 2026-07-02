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

print("press 1 for create a file")
print("press 2 for read a file")
print("press 3 for update to a file")
print("press 4 for delete a file")

check = int(input("please tell your response:- "))

if check == 1:
    createfile()