from pathlib import Path
import shutil
from datetime import datetime
 
# ---------------------------------------------------------------
# STAGE 1: Dictionary mapping instead of if/elif
# ---------------------------------------------------------------
CATEGORIES = {
    ".txt": "Documents",
    ".docx": "Documents",
    ".csv": "Documents",
    ".pdf": "PDFs",
    ".png": "Images",
    ".jpg": "Images",
    ".jpeg": "Images",
}
 
 
def get_category(ext):
    return CATEGORIES.get(ext.lower(), "Others")
 
 
# ---------------------------------------------------------------
# STAGE 2: Duplicate filename handling (photo.png -> photo_1.png)
# ---------------------------------------------------------------
def get_unique_path(target_path):
    new_path = target_path
    counter = 1
    while new_path.exists():
        new_path = target_path.with_name(f"{target_path.stem}_{counter}{target_path.suffix}")
        counter += 1
    return new_path
 
 
# ---------------------------------------------------------------
# STAGE 3: Logging with timestamp
# ---------------------------------------------------------------
def write_log(message):
    with open("organizer.log", "a") as log:
        log.write(message + "\n")
 
 
# ---------------------------------------------------------------
# STAGE 5 (part): dry_run flag inside the organizer
# STAGE 4 (part): counts dictionary, returned at the end
# ---------------------------------------------------------------
def organize_files(folder_path, dry_run=False):
    folder = Path(folder_path)
    counts = {}
 
    for file in list(folder.iterdir()):
        if not file.is_file():
            continue
 
        category = get_category(file.suffix)
        target_folder = folder / category
        target_path = get_unique_path(target_folder / file.name)
 
        if dry_run:
            # Dry run: no folders created, no files moved, no log written
            print(f"Would move: {file.name} -> {category}/{target_path.name}")
        else:
            target_folder.mkdir(parents=True, exist_ok=True)
            shutil.move(str(file), str(target_path))
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            write_log(f"[{timestamp}] Moved: {file.name} -> {category}/{target_path.name}")
 
        counts[category] = counts.get(category, 0) + 1
 
    return counts
 
 
# ---------------------------------------------------------------
# STAGE 4: Summary report
# ---------------------------------------------------------------
def print_summary(counts, dry_run):
    label = "Total would move" if dry_run else "Total moved"
    for category, num in counts.items():
        print(f"{category}: {num}")
    print(f"{label}: {sum(counts.values())}")
 
 
# ---------------------------------------------------------------
# STAGE 5: User input + folder validation + dry-run prompt
# ---------------------------------------------------------------
def main():
    folder_path = input("Enter folder path: ").strip().strip('"')
    folder = Path(folder_path)
 
    if not folder.exists() or not folder.is_dir():
        print("Error: Folder does not exist or is not a directory.")
        return
 
    answer = input("Dry run? (yes/no): ").strip().lower()
    dry_run = answer in ("y", "yes")
 
    counts = organize_files(folder, dry_run)
    print_summary(counts, dry_run)
 
 
if __name__ == "__main__":
    main()
 