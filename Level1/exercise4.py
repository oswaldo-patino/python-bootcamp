def file_countlines(filename : str) -> int:
    """
    Return the number of lines in the specified file

    Parameters:
        filename (str): File name

    Returns:
        count (int): Number of lines
    """
    lines = []
    with open(filename, "r") as file:
        lines = file.readlines()
    count = len(lines)
    return count


def run():
    """
    Runs the exercise 4
    """
    print("##### Exercise 4 #####")
    print("Counts the number of lines in a text file. Enter 'quit' to exit.")
    while True:
        filename = input("Enter the filename: ")
        if filename == "quit":
            break
        try:
            print("{0} lines".format(file_countlines(filename)))
        except IOError:
            print("File not found!")
        except:
            print("An error occurred!")
