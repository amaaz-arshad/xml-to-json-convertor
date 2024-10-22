import json

# Read the JSON data from a file
with open('NBesG_vector.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Copy content of wp_title into title for each object in the array
print(f"Length of the array in the input file: {len(data)}")

for document in data:
    document['title'] = document['wp_title']

# Optionally, save the modified data back to a file
with open('NBesG_vector_title.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

print("Title fields have been updated and saved to 'modified_data.json'.")
