import os

# Define the paths for the source and target folders
source_folder = './images/source'
target_folder = './images/target'

# Get a list of all image files in the source and target folders
source_files = sorted([f for f in os.listdir(source_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))])
target_files = sorted([f for f in os.listdir(target_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))])

# Rename source images
for i, filename in enumerate(source_files):
    new_name = f'image{i + 1}-source.jpg'
    old_path = os.path.join(source_folder, filename)
    new_path = os.path.join(source_folder, new_name)
    os.rename(old_path, new_path)
    print(f"Renamed {filename} to {new_name}")

# Rename target images
for i, filename in enumerate(target_files):
    new_name = f'image{i + 1}-target.jpg'
    old_path = os.path.join(target_folder, filename)
    new_path = os.path.join(target_folder, new_name)
    os.rename(old_path, new_path)
    print(f"Renamed {filename} to {new_name}")

print("Renaming process completed.")