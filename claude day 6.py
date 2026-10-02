from pathlib import Path 

import shutil 

p = Path(".")
print(p)


absolute_path = Path(".").resolve()
print(absolute_path)

direct = Path(".").is_dir()
print(direct)


def file_info(filepath):
    p = Path(filepath)
    return {
        "name": p.name,        
        "extension": p.suffix,
        "parent": p.parent,
        "exists": p.exists()
    }

info = file_info("notes.txt")
print(info)


nested = Path("project/data/raw")
nested.mkdir(parents=True, exist_ok=True)
print("Nested folder created at:", nested.resolve())



txt_files = [f.name for f in Path(".").glob("*.txt")]
print(txt_files)


def organize_files(folder_path):
    folder = Path(folder_path)
    for file in folder.iterdir():
        if file.is_file():
            ext = file.suffix.lower()
            if ext == ".txt":
                target_folder = folder/ "TextFiles"
            elif ext in [".png" , ".jpg" , ".jpeg"]:
                target_folder = folder / "Images"
            elif ext in [".pdf"] :
                target_folder = folder / "PDFs"
            else :
                target_folder = folder / "Others"

            target_folder.mkdir(parents=True, exist_ok=True)
            shutil.move(str(file) , str(target_folder/file.name))

test_folder = Path("test_folder")
test_folder.mkdir(exist_ok=True)

for fname in ["notes.txt" , "report.pdf" , "photo.png" , "data.txt" , "pic.jpg"] :
    (test_folder/fname).write_text("Dummy Content")

organize_files(test_folder)

print("Files organized : ", test_folder.resolve())

def find_largest_file(folder_path):
    folder = Path(folder_path)
    largest_file = None
    largest_size = 0 

    for file in folder.rglob("*"):
        if file.is_file():
            size = file.stat().st_size
            if size > largest_size:
                largest_size = size
                largest_file = file

    if largest_file:
        return {"name" : largest_file.name , "size" : largest_size}
    else :
        return {"name" : None , "size": 0}

result = find_largest_file("test_folder")
print(result)