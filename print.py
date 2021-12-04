import sys
import json

def main():
    if len(sys.argv) != 2:
        print("Usage: print.py trello_export.json")
        exit()

    filename = sys.argv[1]

    with open(filename) as f:
        data = json.load(f)

        for listitem in data["lists"]:
            print("- " + listitem["name"])
            for card in data["cards"]:
                if card["idList"] == listitem["id"]:
                    print("    - " + card["name"])

if __name__ == "__main__":
    main()
