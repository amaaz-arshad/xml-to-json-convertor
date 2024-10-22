import json

# Function to recursively search for "text" keys in a dictionary or list
def extract_text_values(data):
    text_values = []

    if isinstance(data, dict):  # If the data is a dictionary
        for key, value in data.items():
            if key == "text":  # If the key is "text"
                if isinstance(value, str):  # If the value is a string, add it directly
                    text_values.append(value)
                elif isinstance(value, list):  # If the value is a list, iterate through it
                    for item in value:
                        if isinstance(item, str):  # If the item is a string, add it to the list
                            text_values.append(item)
            else:  # Otherwise, recursively search the value
                text_values.extend(extract_text_values(value))
    elif isinstance(data, list):  # If the data is a list
        for item in data:
            text_values.extend(extract_text_values(item))  # Recursively search each item

    return text_values

# Read the JSON file
with open('parsed_NBesG_without_content.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Process each document in the documents array
for document in data.get('documents', []):
    content = document.get('content', {})
    all_text_values = extract_text_values(content)
    concatenated_text = " ".join(all_text_values)
    document['content'] = concatenated_text

# Write the updated JSON back to a file (or overwrite the original file)
with open('NBesG_content_space.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

print("Content fields have been updated and stored in 'updated_json_file.json'.")
