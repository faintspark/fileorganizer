import os
import shutil

folder_map = {
".py": "python",
".txt": "text",
".jpg": "images",
".jpeg": "images",
".png": "images",
".pdf": "documents",
".docx": "documents",
".mp3": "music",
".mp4": "videos"
}

folder = input("Enter folder path: ")

for filename in os.listdir(folder):
    name, ext = os.path.splitext(filename)
    ext == ext.lower()

    if ext == "":
        continue
    if ext in folder_map:
        target_folder = os.path.join(folder, folder_map[ext])
        os.makedirs(target_folder, exist_ok=True)
        source = os.path.join(folder, filename)
        destination = os.path.join(target_folder, filename)
        shutil.move(source, destination)
        print(f"Moveed {filename} -> {folder_map[ext]}")
    else:
        print(f"skipped {filename} (unknown type)")