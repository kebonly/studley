"""Module that summarizes all the changes in a directory"""

import os
import datetime
import time
import pickle

PATH_OBSIDIAN = os.path.expanduser("~") + "/Ushnisha"
PATH_OUTPUT = "activity_report.md"
OMIT = {
    ".DS_Store",
    "Zotero Library Export.bib"
}
PATHS = {
    os.path.expanduser("~") + "/Ushnisha",
    os.path.expanduser("~") + "/Ushnisha/Literature Notes"
}

def save_modified(path_input, modified) -> None:
    with open(path_input, "wb") as f:
        pickle.dump(modified, f)

def load_modified(path_input) -> set:
    if os.path.isfile(path_input):
        with open(path_input, "rb") as f:
            data = pickle.load(f)
        return data
    else:
        return set()

if __name__ == "__main__":
    today = datetime.datetime.today()
    daystart = datetime.datetime(year=today.year, month=today.month, day=today.day, hour=0, second=0)
    path_pickle = f"{os.path.expanduser('~')}/Projects/studley/pickles/{daystart.date()}.pickle"
    prev_res = load_modified(path_pickle)# res = set()
    res = set()
    for dirs in PATHS:
        for filename in os.listdir(dirs):
            modify_time = datetime.datetime.fromtimestamp(os.path.getmtime(f"{dirs}/{filename}"))
            if (modify_time >= daystart) and os.path.isfile(f"{dirs}/{filename}") and (filename not in OMIT):
                if filename[-3:] == ".md":
                    res.add(filename[:-3])
                else:
                    res.add(filename)

    save_modified(path_pickle, res)
    markdown_output = "" #f"\n---\n### Activity report for today\n"
    for i in res - prev_res:
        markdown_output += f"- [[{i}]]\n"
    with open(f"{PATH_OBSIDIAN}/Daily notes/{daystart.date()}.md", "a") as f:
        f.write(markdown_output)
