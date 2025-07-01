from organizer import organize_files

if __name__ == "__main__":
    folder = input("📁 Enter the folder path to organize: ").strip()
    organize_files(folder)