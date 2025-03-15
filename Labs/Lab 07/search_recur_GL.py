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

            


    for path in range(len(paths)):
        if path == len(paths) - 1:
            break
        # print(paths[path].get("checksum"))

        for i in range(path + 1, len(paths)):
            if paths[path].get("checksum") == paths[i].get("checksum"):
                print("Duplicate found!")
                print(paths[path].get("path") + " | Checksum:" + paths[path].get("checksum"))
                print(paths[i].get("path") + " | Checksum:" + paths[i].get("checksum"))

            else:
                print("No duplicates found for File: ", paths[path].get("path"), "and", paths[path].get("checksum"))

            print("\n")
                



def get_checksum(file_path):
    return hashlib.sha256(open(file_path, "rb").read()).hexdigest()


if __name__ == "__main__":
    menu()

    # use .\\a for testing


    # find_duplicates(".\\a")