import json

# Function to count the number of objects with an empty "counter" field
def count_empty_counter(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)  # Load JSON data from file
        
        if not isinstance(data, list):
            raise ValueError("The JSON data is not an array.")
        
        empty_counter_count = 0  # Counter for objects with empty "counter"
        
        for obj in data:
            # Check if "counter" exists and is an empty string
            if obj.get("content") == "":
                empty_counter_count += 1
        
        return empty_counter_count

# Example usage
file_path = 'NBesG_new_docs_only.json'  # Replace with your actual file path
empty_counter_count = count_empty_counter(file_path)

# Output the result
print(f"Number of objects with empty 'counter' field: {empty_counter_count}")
