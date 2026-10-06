from pathlib import Path
import shutil

from datetime import datetime

CATEGORIES = {
    ".txt": "Documents",
    ".docx": "Documents",
    ".csv": "Documents",
    ".pdf": "PDFs",
    ".png": "Images",
    ".jpg": "Images",
    ".jpeg": "Images",
}

test_folder = Path("test_folder")
test_folder.mkdir(exist_ok=True)

for fname in ["notes.txt", "report.pdf", "photo.png"]:
    (test_folder / fname).write_text("Dummy content")

def main():
    folder_path = input("Enter folder path :").strip().strip(" ")
    fldr = Path(folder_path)

    if not fldr.exists() or not fldr.is_dir():
        print("Error ! Folder not exists")
        return 

    answer = input("Dry run ? (Yes / No )") .strip().lower()
    dry_rn = answer in ("y" , "yes")

    counts = organize_files(fldr , dry_rn)
    print_summary(counts, dry_rn)

if __name__ == "__main__":
    main()


def get_category(ext):
    return CATEGORIES.get(ext.lower() , "Others")


def get_unique_path(target_path):
    new_path = target_path
    counter = 1 
    while new_path.exists():
        new_path = target_path.with_name(f"{target_path.stem}_{counter}{target_path.suffix}")
        counter += 1 
    return new_path


def write_log(message):
    with open ("organizer.log" , "a") as f :
        f.write(f"{message}\n")


def organize_files(folder_path, dry_run):
    folder = Path(folder_path)
    count = {}

    for file in list(folder.iterdir()):
        if not file.is_file():
            continue
        category = get_category(file.suffix)
        target_folder = folder / category
        target_path = get_unique_path(target_folder/file.name)
        print(file.name, "->", category)

        if dry_run:
            print(f"Would move {file.name} -> {category}/{target_path.name}")
        else :
            target_folder.mkdir(parents=True , exist_ok=True)
            shutil.move(str(file) , str(target_path))
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            write_log(f"[{timestamp}] Moved: {file.name} -> {category}/{target_path.name}")

        count[category] = count.get(category,0) + 1 

    return count


result = organize_files("test_folder", False)  # normal

print(result)


def print_summary(counts, dry_run):
    label = "Total would move" if dry_run else "Total moved"
    for category , num in counts.items():
        print(f"{category} : {num}")
    print(f"{label} : {sum(counts.values())}")

if __name__ == "__main__":
    main()