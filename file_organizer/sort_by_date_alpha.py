import os
import shutil
from datetime import datetime

def organize_by_date(folder_path):
    if not os.path.isdir(folder_path):
        print("Invalid folder path.")
        return

    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        if os.path.isfile(file_path):
            # Get file creation/modification date
            mod_time = os.path.getmtime(file_path)
            date_folder = datetime.fromtimestamp(mod_time).strftime("%Y-%m-%d")
            dest_dir = os.path.join(folder_path, date_folder)

            os.makedirs(dest_dir, exist_ok=True)
            shutil.move(file_path, os.path.join(dest_dir, file))

    print("✅ Files sorted by date.")

def organize_by_alpha(folder_path):
    if not os.path.isdir(folder_path):
        print("Invalid folder path.")
        return

    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        if os.path.isfile(file_path):
            first_char = file[0].upper()
            if not first_char.isalpha():
                first_char = "Others"
            dest_dir = os.path.join(folder_path, first_char)

            os.makedirs(dest_dir, exist_ok=True)
            shutil.move(file_path, os.path.join(dest_dir, file))

    print("✅ Files sorted alphabetically.")