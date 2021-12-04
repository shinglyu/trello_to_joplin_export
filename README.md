# Export Trello to Joplin

Here are some scripts that allows you to export your trello board to Jopin. You can then use the [Kanban](https://github.com/joplin/plugin-kanban/wiki) plugin to create a kanban board.

# Usage 
* Go to your Trello board. Board Menu > More > Print and export > Export as JSON. (reference: [Official doc](https://help.trello.com/article/747-exporting-data-from-trello-1))
* Run 
    ```
    python3 convert_to_dir.py export.json # export.json is the JSON you exported in the previous step
    ```
* A folder with the same name of your board will be created, containing one subfolder for each list, and one `.md` file for each card.
* Go to Joplin > File > Import > MD - Markdown (Directory) > Select the generated folder

# Alternative usage:
If you just want a list of your cards as a markdown bullet point list.  Run
```
python3 print export.json
```

# Caveats
* Doesn't support images, checklist, attachments, etc.
* Long file name will be trimmed.
* Doesn't support Joplin tags. For that you need to convert to a more advanced format like ENEX or JEX.
* Only tested on Linux (Ubuntu 20.04) with EXT4. You mileage might very if you use different OS and file system because of filename format limitations.

