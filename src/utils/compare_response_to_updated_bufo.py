from read_response import read_response
from get_updated_bufo import get_filenames_in_directory


emoji_names = read_response()
file_names = get_filenames_in_directory('all_bufo_updated')


# Convert lists to sets for easier comparison
filenames_set = set(file_names)
emoji_names_set = set(emoji_names)

# Find the difference - files in directory not in emoji_names
difference = filenames_set - emoji_names_set
print("list of different emoji")
print(list(difference))



