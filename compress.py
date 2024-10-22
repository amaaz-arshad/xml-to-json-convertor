import json

# Read the JSON file
with open('documents_only.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Write the compressed JSON back to a new file without indentation
with open('documents_only_compressed.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False)  # Default is no indent, producing a compact file

print("Compressed JSON file has been stored in 'documents_only_compressed.json'.")
