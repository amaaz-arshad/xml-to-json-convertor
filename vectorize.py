import json
from sentence_transformers import SentenceTransformer

# Load the SentenceTransformer model
model = SentenceTransformer('sangmini/msmarco-cotmae-MiniLM-L12_en-ko-ja')

# Read the JSON file
with open('NBesG_new_docs_only.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Process each document in the documents array
for document in data.get('documents', []):
    # Process wp_title and create vectorTitle
    wp_title = document.get('title', '')
    if wp_title:  # Only encode if wp_title is not empty
        vector_title = model.encode(wp_title, show_progress_bar=True).tolist()  # Generate and store the embedding as a list
        document['vectorTitle'] = vector_title

    # Process content and create vectorContent
    content = document.get('content', '')
    if content:  # Only encode if content is not empty
        vector_content = model.encode(content, show_progress_bar=True).tolist()  # Generate and store the embedding as a list
        document['vectorContent'] = vector_content

# Write the updated JSON back to a file (or overwrite the original file)
with open('NBesG_new_docs_only2.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=1)

print("Embeddings have been stored in 'NBesG_vectorized.json'.")
