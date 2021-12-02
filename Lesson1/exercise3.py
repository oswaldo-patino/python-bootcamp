def get_file_extension(filename : str) -> str:
    splitted = filename.split(".")
    if len(splitted) > 0:
        return splitted[1]
    else:
        return "No file extension"

def run():
    print("##### Exercise 3 #####")
    print("Get extension of a file. Enter 'quit' to exit.")
    while True:
        filename = input("File name: ")
        if filename == "quit":
            break
        print(get_file_extension(filename))