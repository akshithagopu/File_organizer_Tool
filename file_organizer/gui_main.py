import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox
from config import FILE_TYPES

def get_file_category(file_name):
    ext = os.path.splitext(file_name)[1].lower()
    for category, extensions in FILE_TYPES.items():
        if ext in extensions:
            return category
    return "Others"

def organize_files(folder_path):
    if not os.path.isdir(folder_path):
        messagebox.showerror("Error", "Invalid folder path")
        return

    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        if os.path.isfile(file_path):
            category = get_file_category(file)
            dest_dir = os.path.join(folder_path, category)
            os.makedirs(dest_dir, exist_ok=True)
            shutil.move(file_path, os.path.join(dest_dir, file))

    messagebox.showinfo("Success", "Files organized successfully")

def browse_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        organize_files(folder_selected)

def create_gui():
    root = tk.Tk()
    root.title("File Organizer Tool")
    root.geometry("300x150")

    label = tk.Label(root, text="Organize your folder files by type", padx=10, pady=10)
    label.pack()

    browse_btn = tk.Button(root, text="Choose Folder", command=browse_folder, padx=10, pady=5)
    browse_btn.pack()

    root.mainloop()

if __name__ == "__main__":
    create_gui()