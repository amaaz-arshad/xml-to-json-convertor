import json

# Read the JSON file
with open('NBesG_content_space.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Extract the "documents" array
documents = data.get('documents', [])

# Write the "documents" array to a new JSON file
with open('NBesG_content_space_docs.json', 'w', encoding='utf-8') as file:
    json.dump(documents, file, ensure_ascii=False, indent=1)

print("Documents array has been stored in 'documents_only.json'.")
