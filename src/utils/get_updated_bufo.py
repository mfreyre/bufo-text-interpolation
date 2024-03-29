import os
import shutil

# Define your directories here
dir_one = 'all_bufo_updated'
dir_two = 'bufo_i_have_uploaded'
dir_three = 'to_be_uploaded'

# # Ensure dir_three exists
# if not os.path.exists(dir_three):
#     os.makedirs(dir_three)

# List all files in the first and second directories
files_in_dir_one = {file for file in os.listdir(dir_one) if os.path.isfile(os.path.join(dir_one, file))}
print(f"files in dirone: {files_in_dir_one}")
files_in_dir_two = {file for file in os.listdir(dir_two) if os.path.isfile(os.path.join(dir_two, file))}

# Determine files in dir_one but not in dir_two
files_to_copy = files_in_dir_one - files_in_dir_two

# Copy the files to the third directory
for file in files_to_copy:
    shutil.copy(os.path.join(dir_one, file), dir_three)

print(f"Files copied to {dir_three}: {files_to_copy}")
