import os

basedir = r"X:\Tutorial's\Web\Udemy - Node.js, Express, MongoDB & More The Complete Bootcamp 2020 2019-12"
# Test Dir
# basedir = r"C:\Users\Jay\Desktop\test"


def rename(oldPath, oldName):
    if oldName[0].isdigit() and oldName[1] == ".":
        newName = "0" + oldName
        newPath = oldPath.replace(oldName, newName)
        os.replace(oldPath, newPath)
        print("Done", oldPath)


def doTheTask():
    for root, subdirectories, files in os.walk(basedir):
        for subdirectory in subdirectories:
            rename(os.path.join(root, subdirectory), subdirectory)
        for file in files:
            rename(os.path.join(root, file), file)


doTheTask()
# Repeat the task, for selecting files after renaming the folders
doTheTask()

print("Done")
