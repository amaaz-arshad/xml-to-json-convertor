import json

# Function to read JSON file and return the length of the array
def get_json_array_length(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)  # Load JSON data from file
        if isinstance(data, list):  # Check if the data is an array (list)
            return len(data)
        else:
            raise ValueError("The JSON data is not an array.")

# Example usage
file_path = 'NBesG_new_docs_only.json'  # Replace with your actual file path
try:
    array_length = get_json_array_length(file_path)
    print(f"The length of the JSON array is: {array_length}")
except ValueError as e:
    print(e)
