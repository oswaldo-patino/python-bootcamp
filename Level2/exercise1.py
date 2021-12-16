import os

def list_directory(dir: str):
    """
    Return a list of the files and subdirectories

    Parameters:
        dir (str): Directory
    """
    print("{0:30s} {1:5s}".format("Name", "Type"))
    print("{0:30s} {1:5s}".format("-"*30, "-"*5))
    for subdir in os.listdir(dir):
        path = os.path.join(dir, subdir)
        if os.path.isdir(path):
            print("{0:30s} {1:5s}".format(subdir, "dir"))
        else:
            print("{0:30s} {1:5s}".format(subdir, "file"))
    print()

def run():
    """
    Runs the exercise 1
    """
    print("##### Exercise 1 #####")
    print("List the specified directory. Enter 'quit' to exit.")
    while True:
        dir = input("Enter the directory: ")
        if dir == "quit":
            break
        try:
            list_directory(dir)
        except Exception as e:
            print("An error ocurred:", format(e))