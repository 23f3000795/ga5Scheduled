import json
# Input data (this is your original list)
with open('movie data.json', 'r') as file:
    data = json.load(file)

# Convert the array of arrays into an array of objects (dictionaries)
result = [
    {
        "id": item[0],
        "title": item[1],
        "year": item[2],
        "rating": item[3]
    }
    for item in data
]

# Print the result in the desired format
for entry in result:
    print(f'{{ "id": "{entry["id"]}", "title": "{entry["title"]}", "year": "{entry["year"]}", "rating": "{entry["rating"]}" }},')
