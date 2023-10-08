from pathlib import Path
import os
import time


def list_dir(directory, items=False, folders=False, numbered=False):
    directory = Path(directory)
    dir_text = []

    directories = []
    items_list = []

    for i in directory.iterdir():
        name = i.name
        if i.is_dir():
            dir_text.append(f"\033[94m{name}\033[0m")  # ANSI code makes text light blue
            directories.append(f"\033[94m{name}\033[0m")
        else:
            dir_text.append(name)
            items_list.append(name)

    # Modify output based on keyword arguments
    if items == True:
        return ", ".join(items_text)

    elif folders == True:
        return ", ".join(directories)

    elif len(dir_text) < 1:
        return "No items in this directory."

    else:
        if numbered:
            x = 1
            for i in dir_text:
                print(f"{x}.", i)
                x += 1
        else:
            return (
                ", ".join(dir_text)
                if len(dir_text) < 10
                else "More than 10 items, View items individually to see them."
            )


def create_dir(name):
    directory = Path(name)

    if directory.exists():
        print("This directory already exists")
        input("...")
    else:
        directory.mkdir()


def change_dir(directory):
    path = Path(directory)

    os.chdir(path)


def search_for(filename, directory):
    directory = Path(directory)
    match_count = 0
    file_list = []

    for i in directory.iterdir():
        if filename.lower() in i.name.lower():
            name = i.name.lower()

            # Shorten display name if filename is too long
            if len(name) > 20:
                name = f"{i.name[:40]}..."

            file_list.append(name)
            match_count += 1
        else:
            pass

    if match_count > 0:
        print("\n", match_count, "match(es) found:\n")
        print("\n".join(file_list))
        input("...")
    else:
        print("No results found.")
        input("...")
