import os
import shutil

def move_jpg_files(source_folder, destination_folder):
    files = os.listdir(source_folder)
    for file in files:
        if file.endswith('.txt'): # file format
            source_path = os.path.join(source_folder, file)
            destination_path = os.path.join(destination_folder, file)
            shutil.move(source_path, destination_path)
            print(f"Moved file: {file}")




source_folder = 'source'
destination_folder = 'destination'
move_jpg_files(source_folder, destination_folder)
