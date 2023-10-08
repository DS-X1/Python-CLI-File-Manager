import os
import shutil
from pathlib import Path


def copy_file(filename, destination_path):
    try:
        file = Path(filename)
        destination_path = Path(destination_path)

        if file.is_dir() is True:
            print("\n File must exist and not be a folder.")
            input("...")
        elif destination_path.is_dir() is False:
            print("\n Must copy to a folder that exists.")
            input("...")

        elif destination_path == Path.cwd():
            shutil.copy(file.absolute(), destination_path.absolute())
        else:
            shutil.copy(file.absolute(), destination_path.absolute())

    except shutil.SameFileError:
        print("File already exists here.")
        input("...")

    except FileNotFoundError:
        print("Path doesn't exist or wasn't given.")
        input("...")


def create_file(filename):
    file = Path(filename)

    if file.exists():
        print("This file already exists")
        input("...")
    else:
        file.touch()


def move_file(source_path, destination_path):
    original_file = Path(source_path)

    if original_file.samefile(destination_path) is True:
        print(f"\n{original_file.name} already exists in {destination_path}.")
        input("...")
        return
    else:
        shutil.copy(source_path, destination_path)
        original_file.unlink()


def rename_file(file, new_name):
    target_file = Path(file)
    target_file.rename(new_name)


def delete_file(file):
    target_file = Path(file)

    if target_file.exists():
        if target_file.is_dir():
            shutil.rmtree(target_file)
        else:
            target_file.unlink()
    else:
        print("This file doesn't exist.")
        input("...")


def view_file(file):
    file = Path(file)
    print(file.read_text())
    input("")
