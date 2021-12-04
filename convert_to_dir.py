import sys
import os
import json

def cleanFilename(rawFilename):
    return rawFilename.replace("/", "_").replace(":", "_")[0:50]

def main():
    if len(sys.argv) != 2:
        print("Usage: convert_to_dir.py trello_export.json")
        exit()

    filename = sys.argv[1]

    with open(filename) as f:
        data = json.load(f)

        boardName = cleanFilename(data["name"])

        if not os.path.exists(boardName):
            os.mkdir(boardName)

        for listitem in data["lists"]:
            print("- " + listitem["name"])

            listPath = os.path.join(boardName, cleanFilename(listitem["name"]))
            if not os.path.exists(listPath):
                os.mkdir(listPath)
            for card in data["cards"]:
                if card["idList"] == listitem["id"]:
                    print("    - " + card["name"])
                    cardName = cleanFilename(card["name"]) + (" [CLOSED]" if card["closed"] else "")
                    print("        => " + os.path.join(listPath, cardName+ ".md"))
                    with open(os.path.join(listPath, cardName+ ".md"), 'w') as f:
                        f.write(
"""# {title} {closed}

{body}

Exported from {shortUrl}
""".format(
    title=card["name"],
    body=card["desc"],
    shortUrl=card["shortUrl"],
    closed="[CLOSED]" if card["closed"] else ""
))

if __name__ == "__main__":
    main()
