import os
import shutil
from config import FILE_TYPES

def get_file_category(file_name):
    ext = os.path.splitext(file_name)[1].lower()
    for category, extensions in FILE_TYPES.items():
        if ext in extensions:
            return category
    return "Others"

def organize_files(folder_path):
    if not os.path.isdir(folder_path):
        print("Invalid folder path.")
        return

    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)

        if os.path.isfile(file_path):
            category = get_file_category(file)
            dest_dir = os.path.join(folder_path, category)

            os.makedirs(dest_dir, exist_ok=True)
            shutil.move(file_path, os.path.join(dest_dir, file))

    print("✅ Files organized successfully.")