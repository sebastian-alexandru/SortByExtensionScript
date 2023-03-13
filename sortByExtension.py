# used libraries
import os
import shutil
import pathlib

# set the path of the folder that will be sorted
currentDirectory = os.getcwd()
path = currentDirectory + "/fisiere/"

# create a list of all files inside 'path' folder
filenames = os.listdir(path)

# sort list 'filenames' by key (fileExtension) and assign to dictionary
# for folders and for files that have no extension no further action will be performed
extensionToFilesDict = {}
for i in range(len(filenames)):
    fileExtension = pathlib.Path(filenames[i]).suffix
    if fileExtension == '':
        continue
    if fileExtension in extensionToFilesDict:
        extensionToFilesDict[fileExtension].append(filenames[i])
    else:
        extensionToFilesDict[fileExtension] = [filenames[i]]

# show all existing folders, if any, inside 'path' folder
existingFolders = next(os.walk(path))[1]
if len(existingFolders) == 0:
    print("There are no existing folders")
else: 
    print("The current existing folders are: ")
    for i in existingFolders:
        print (i)

# based on 'fileExtension' choose or create a folder and move each file to the folder corresponding to its extension
for key in extensionToFilesDict:
    selectFolder = input("To which folder would you like to assign "+ key +" type files? (if the folder doesn't exist, it will be created)")
    if not os.path.exists(path+selectFolder):
        os.makedirs(path+selectFolder)
    for element in extensionToFilesDict[key]:
        shutil.move(path+element, path+selectFolder+"/"+element)