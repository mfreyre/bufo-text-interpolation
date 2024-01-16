import os

def get_phrases_from_file(filename):
    with open(filename, 'r') as file:
        phrases = [line.strip() for line in file]
    return phrases


def get_emoji_names():
    directory_path = 'bufo-images/'  # Replace with your directory path

    # Set the output file name
    output_file_name = 'emoji-names.txt'

    # List to hold file names
    file_names = []

    # Read the file names in the directory
    for file in os.listdir(directory_path):
        if os.path.isfile(os.path.join(directory_path, file)):
            name, _ = os.path.splitext(file)  # Split the name and extension, ignore the extension
            file_names.append(name)

    # Write the file names without extensions to the output file
    with open(output_file_name, 'w') as file:
        for name in file_names:
            file.write(name + '\n')


    print(f"File names written to {output_file_name}")