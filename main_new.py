import os

source_folder = input("Enter folder path: ").strip()

# Check if folder exists
if not os.path.exists(source_folder):
    print("Folder does not exist!")
    exit()

# Get all items and sort them
files = os.listdir(source_folder)
files.sort() 

prefix = input("Enter prefix for renaming files: ").strip()

start_num = int(input("Enter starting number: "))

renamed_count = 0

for i, file in enumerate(files, start=start_num):

    old_path = os.path.join(source_folder, file)

    # Skip folders
    if not os.path.isfile(old_path):
        continue

    # Separate filename and extension
    name, ext = os.path.splitext(file)

    # Create new filename
    new_name = f"{prefix}_{i:02}{ext}"

    # Create full new path
    new_path = os.path.join(source_folder, new_name)

    # Skip if same filename already exists
    if os.path.exists(new_path):
        print(f"Skipping {file} -> {new_name} already exists")
        continue

    # Rename file
    os.rename(old_path, new_path)

    renamed_count += 1

    print(f"{file} renamed to {new_name}")

print("-" * 40)
print(f"{renamed_count} files renamed successfully")