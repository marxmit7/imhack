import pathlib

# Blacklisted folders to ignore when contructing index
BLACKLIST = [
    ".git"
]
NO_DESC_MESSAGE = "No description provided."

template = """
# Pyamit
A Python practise repository!

## Structure
Each script/topic goes inside it's own folder with a README.md
Line 1 of the README should be a H1 title of the script/topic
Line 3 of the README should be a H2 short description

Folders must **not** have spaces in the name otherwise the folder links **will not work**

**ALWAYS RUN `update.py` BEFORE PUSHING COMMITS**

e.g.
```
# Project title

## Short description of this project
```

## Index

"""

index = ""
print("Loading folders")
uselessFolder = pathlib.Path(".")
folders = [f for f in uselessFolder.iterdir() if f.is_dir()]
for folder in folders:
    if folder.name in BLACKLIST:
        continue
    print(f"Collecting data for folder {folder}")
    try:
        with open(f"{folder}/README.md") as f:
            data = f.readlines()
            desc = data[2]
            if desc[:2] != "##":
                desc = NO_DESC_MESSAGE
            else:
                desc = desc.replace("#", " ").strip()
            name = data[0]
            if name[0] != "#":
                name = folder.name
            else:
                name = name.replace("#", " ").strip()

    except FileNotFoundError:
        desc = NO_DESC_MESSAGE
        name = folder
    index_entry = f"[{name}]({folder}) - {desc}\n\n"
    template += index_entry

with open("README.md", "w") as f:
    f.write(template)

print("Updated README.md index!")
input("Press enter to continue. . .")
