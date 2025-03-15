import os
import hashlib

def menu():
    while True:
        print("\n--- File Duplicate Finder ---")
        print("1. Enter directory to search")
        print("2. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            directory = input("Enter the directory to search: ")
            find_duplicates(directory)
        elif choice == "2":
            break
        else:
            print("Invalid choice. Try again.")

def find_duplicates(directory):
    # search os.walk(directory):

    paths = []
    print("Searching for duplicates in", directory)
    for root, _, files in os.walk(directory):

        for file in files:


            file_path = os.path.join(root, file)

            # print(file_path
            print(file_path)

            print(get_checksum(file_path))

            paths.append(
                {
                    "path": file_path,
                    "filename": file,
                    "checksum": get_checksum(file_path)
                }
            )

            print(paths)


    for path in paths:
        print(path)

        



    # use a dictionary to store file names and paths
    # compare files with the same name

def get_checksum(file_path):
    return hashlib.sha256(open(file_path, "rb").read()).hexdigest()


if __name__ == "__main__":
    # menu()

    # use .\\a for testing


    find_duplicates(".\\a")