import json

data = {
    "H": 1.008,
    "He": 4.0026,
    "Li": 6.94,
    "Be": 9.0122,
    "B": 10.81,
}

with open('elements.json', 'w') as json_file:
    json.dump(data, json_file)

print("Дані про хімічні елементи були збережені у файлі 'elements.json'.")
