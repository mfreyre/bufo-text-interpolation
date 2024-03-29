from read_response import read_response
from get_updated_bufo import get_filenames_in_directory, copy_files_into_dir

emoji_names = []
for i in range(1, 11):
    emoji_names += read_response(f"response{i}")
    # Read the JSON file
    with open('current.txt', 'w+') as file:
        file.writelines([f"{line}\n" for line in emoji_names])


file_names = get_filenames_in_directory('all_bufo_updated')


# Convert lists to sets for easier comparison
print(f"emoji names first ten are {emoji_names[:10]} and the length is {len(emoji_names)}")
print(f"file names first ten are {file_names[:10]} and the length is {len(file_names)}")
filenames_set = set(file_names)
emoji_names_set = set(emoji_names)

# Find the difference - files in directory not in emoji_names
difference = filenames_set - emoji_names_set
print("list of different emoji")
files_to_copy = sorted(list(difference))
for emoji in files_to_copy:
    print(emoji)

print(f"the length of difference is {len(difference)}")

copy_files_into_dir(files_to_copy, 'all_bufo_updated', 'to_be_uploaded')