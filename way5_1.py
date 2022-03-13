"# yam-mesika-weeks-3-4-hadasa-web"
import glob
import os
import re


# "C:\Users\ha054\Downloads\trying"
def listfile():
    path = input("enter a path\n")
    pathlist = path.split("\\")
    list_of_file = []
    # prefix = "image.*"
    for i in os.listdir(path):
        if "deep" in i:
            if os.path.isfile(os.path.join(path, i)):
                list_of_file.append(i)
    if pathlist[-1] == "image":
        if len(list_of_file) != 2:
            list_of_file = []
            print("The folder does not contain 2 files")
    return list_of_file

print(listfile())
