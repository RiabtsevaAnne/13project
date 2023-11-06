import json

def data(filename):
    with open(filename) as json_file:
        elements_data = json.load(json_file)
    return elements_data

jsonfile = 'elements.json'

elements = data(jsonfile)

s = {k: v for k, v in sorted(elements.items(), key=lambda item: item[1], reverse=True)}

print("Відсортований словник за відносною атомною масою у порядку спадання:")
for element, mass in s.items():
    print(f"{element}: {mass}")

