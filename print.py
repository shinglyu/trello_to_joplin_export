import json

# Set file here:
filename = "Learning.json"

with open(filename) as f:
    data = json.load(f)

    for listitem in data["lists"]:
        print("- " + listitem["name"])
        for card in data["cards"]:
            if card["idList"] == listitem["id"]:
                print("    - " + card["name"])

