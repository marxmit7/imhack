import pathlib
import requests

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

contributor_template = """
# Contributors

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

r = requests.get("https://api.github.com/repos/amit2rockon/pymit/contributors")
if r.status_code == 200:
    contributors = r.json()
    for contributor in contributors:
        username = contributor["login"]
        url = contributor["url"].replace("api.", "www.").replace("users/", "")
        print(f"{username}: {url}")
        contributor_template += f"[{username}]({url})   \n"
else:
    print(f"{r.status_code}: Error making request for contributors")

with open("CONTRIBUTORS.md", "w") as f:
    f.write(contributor_template)

input("Press enter to continue. . .")
