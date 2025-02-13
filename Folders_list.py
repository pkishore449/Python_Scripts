#This code prints list of files present in the given folders.
import os
folders_list=input("Enter folder names with space between them:").split(',')
for i in folders_list:
    try:
        files=os.listdir(i)
    except FileNotFoundError:
        print(i," folder not found. Please enter valid file name")
        continue #try with break also.But it will terminate if folder not valid.Continue Will skip that folder.
    print("*********The files in the ",i,"are: ")
    for j in files:
        print(j)

***************************************************************************************************************************************

import os

def folders():
    folder_list=input("Please enter folder names with space between:").split()
    for i in folder_list:
        try:
            files=os.listdir(i)
        except FileNotFoundError:
            print(i,"Folder not exists. Please provdide valid folder name")
            continue
        for j in files:
            print(j)

folders()
