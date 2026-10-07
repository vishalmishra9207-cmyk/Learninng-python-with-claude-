import shutil
import os
from pathlib import Path 
import sys

def copy_file():
    with open("sample.txt" , "w") as f:
        f.write("Learnig shuttil , os, patthlib module !")

    shutil.copy("sample.txt" , "sample_copy.txt")

    files = os.listdir(".")
    print("file with os.listdir : " ,files)

    current_dir = Path(".")
    print("Pathlib files")
    for file in current_dir.iterdir():
        print(file.name)

copy_file()


def copy_file():
    shutil.copy("sample.txt", "sample_copy.txt")
    print("sample.txt exists:", os.path.exists("sample.txt"))
    print("sample_copy.txt exists:", os.path.exists("sample_copy.txt"))

copy_file()

shutil.copytree("test_os_folder" , "test_os_folder_back",dirs_exist_ok=True)
print(os.path.exists("test_os_folder_backup"))

backup_folder = "test_os_folder_backup"
shutil.copytree("test_os_folder", backup_folder, dirs_exist_ok=True)
print(os.path.exists(backup_folder))

backup_folder = "test_os_folder_backup"
shutil.copytree("test_os_folder", backup_folder, dirs_exist_ok=True)
print(os.path.exists(backup_folder))

os.remove("sample.txt")
print("sample_copy.txt exists after delete " , os.path.exists("sample_copy.txt"))

# shutil.rmtree("test_os_folder_back")
# print("back up folder exists after delete : " , os.path.exists("test_os_folder_back"))

total , used , free = shutil.disk_usage(".") 

print("Total : "  , total // (1024 ** 3) , "GB")
print("Free : " , free // (1024 ** 3) ,"GB")
print("Used : " , used // (1024 ** 3) , "GB")


