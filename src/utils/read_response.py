import json


def read_response():
    # Path to your JSON file
    file_path = 'src/utils/response.json'

    # Read the JSON file
    with open(file_path, 'r') as file:
        data = json.load(file)

    # Extract the names of the emoji objects
    emoji_names = []
    for emoji in data['emoji']:
        name = emoji['name']
        url = emoji['url']
        extension = url.split('.')[-1]  # Gets the part of the URL after the last '.'
        emoji_names.append(f"{name}.{extension}")

    return emoji_names

