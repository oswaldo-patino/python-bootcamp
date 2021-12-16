def file_countwords(filename : str) -> dict:
    """
    Return the frequency per word in the specified file

    Parameters:
        filename (str): File name

    Returns:
        frequencies (dict): Frequency per word
    """
    frequencies = {}
    with open(filename, "r") as file:
        lines = file.read().splitlines()
        for line in lines:
            words = line.split(" ")
            for word in words:
                if word in frequencies:
                    frequencies[word] += 1
                else:
                    frequencies[word] = 1

    return frequencies

def run():
    """
    Runs the exercise 5
    """
    print("##### Exercise 5 #####")
    print("Gets the frequency of words in a text file. Enter 'quit' to exit.")
    while True:
        filename = input("Enter the filename: ")
        if filename == "quit":
            break
        try:
            print(file_countwords(filename))
        except IOError:
            print("File not found!")
        except:
            print("An error occurred!")