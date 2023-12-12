import os
import shutil
import time

current_directory = os.getcwd()

last_24hours_folder = os.path.join(current_directory, "last_24hours")
if not os.path.exists(last_24hours_folder):
    os.makedirs(last_24hours_folder)

current_time = time.time()

for root, dirs, files in os.walk(current_directory):
    for file in files:
        file_path = os.path.join(root, file)

        creation_time = os.path.getctime(file_path)
        modification_time = os.path.getmtime(file_path)

        if current_time - creation_time <= 24 * 60 * 60 or current_time - modification_time <= 24 * 60 * 60:
            updated_file_path = os.path.join(last_24hours_folder, f"updated_{file}")
            shutil.copy2(file_path, updated_file_path)