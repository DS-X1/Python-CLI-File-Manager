import os
from pathlib import Path

from file_operations import *
from folder_operations import *


def clear():
    os.system("cls" if os.name == "nt" else "clear")


if __name__ == "__main__":
    while True:
        clear()

        directory = Path.cwd()
        directory_path = directory.absolute()
        parent_dir = directory.parent.name

        if list_dir(directory):
            file_list = list_dir(directory)
        else:
            file_list = "No items in this directory."

        text = f"""
	Current Directory: {directory}

		Files:
	{file_list}


		Type a number and hit 'enter'.

		0. View all directory items

		1. Create a new directory or file
		2. Change the current directory
		3. Copy a file
		4. Move a file or directory
		5. Rename a file or directory
		6. Delete a file or directory
		7. Search for a file in a directory
		8. View the contents of a file
		9. About

		/{parent_dir}> """

        choice = input(text)

        if choice == "0":
            clear()

            list_dir(directory, numbered=True)
            input("\n ...")

        elif choice == "1":
            clear()

            filetype = input("'folder' to make a folder, 'file' to make a file: ")

            if filetype == "folder":
                directory_name = input("Name of directory to make: ")

                if directory_name:
                    create_dir(directory_name)

            elif filetype == "file":
                file_name = input("Name of file to create: ")

                if file_name:
                    create_file(file_name)

        elif choice == "2":
            clear()
            print(f"\n{list_dir(directory,folders=True)}\n")
            print(
                "\nTip: This is basically 'cd'. You may type '..' to go to the parent directory, etc.\n"
            )

            directory_name = input("Name of directory to change to (cd): ")

            try:
                change_dir(directory_name)
            except FileNotFoundError:
                print("The directory doesn't exist.")
                input("...")

        elif choice == "3":
            clear()

            print("Current Directory:", directory_path, "\n")
            print("Files: \n", list_dir(directory))

            filename = input("\nEnter name of file to copy: ")
            destination_path = input("Enter path to paste to: ")

            if filename:
                copy_file(filename, destination_path)
            else:
                input("No file was given to copy.")

        elif choice == "4":
            clear()

            print("Current Directory:", directory_path, "\n")
            print("Files: \n", list_dir(directory))

            source_path = input("\nEnter path of file to move: ")
            destination_path = input("Enter path to move to: ")

            if source_path and destination_path:
                move_file(source_path, destination_path)
            else:
                input("\nSome fields are missing.")

        elif choice == "5":
            clear()

            print("Current Directory:", directory_path, "\n")
            print("Files: \n", list_dir(directory))

            source_path = input("\nName or path of file to rename: ")
            new_name = input("Rename to: ")

            if source_path and new_name:
                rename_file(source_path, new_name)
            else:
                input("\nSome fields are missing.")

        elif choice == "6":
            clear()

            print("Current Directory:", directory_path, "\n")
            print("Files: \n", list_dir(directory))

            source_path = input("\nName or path of file to delete: ")

            if source_path:
                delete_file(source_path)
            else:
                input("\nNo file entered.")
                continue

        elif choice == "7":
            clear()

            print("Current Directory:", directory_path, "\n")

            filename = input("Search for filename: ")
            source_directory = input("in directory (leave blank to search current): ")

            search_for(filename, source_directory)

        elif choice == "8":
            clear()

            print("Files: \n", list_dir(directory))

            target_file = input("\nEnter name or path of file: ")

            if target_file:
                clear()
                view_file(target_file)
            else:
                input("\nNo file entered.")

        elif choice == "9":
            clear()

            input(
                "ALL GLORY TO THE LORD\n\nThis is a CLI File Manager written in Python as a personal project.\n..."
            )

        else:
            continue
