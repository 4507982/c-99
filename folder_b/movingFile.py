import os
import shutil
source = input("enter sorce folder name: ")
destenation = input("enter destenation folder name: ")
source = source+"/"
destenation = destenation+"/"
listOfFiles = os.listdir(source)
for file in listOfFiles:
    shutil.move((source+file),destenation)
