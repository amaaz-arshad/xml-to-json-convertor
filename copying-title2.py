import json

# Read the JSON data from the file
with open('old_parsed_NBesG.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Extract the "documents" array
documents = data.get('documents', [])

# Copy content of wp_title into title for each document in the "documents" array
for document in documents:
    document['title'] = document['wp_title']

# Save the modified data back to a new JSON file
with open('old_parsed_NBesG_title.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

print("Title fields have been updated and saved to 'modified_data.json'.")
