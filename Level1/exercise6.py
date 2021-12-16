def countchars(text : str) -> dict:
    """
    Return the frequency of characters in the specified text

    Parameters:
        text (str): Single text

    Returns:
        frequencies (dict): Frequency per character
    """
    frequencies = {}
    for char in text:
        if char in frequencies:
            frequencies[char] += 1
        else:
            frequencies[char] = 1

    return frequencies

def run():
    """
    Runs the exercise 6
    """
    print("##### Exercise 6 #####")
    print("Gets the frequency of characters in an input text. Enter 'quit' to exit.")
    while True:
        text = input("Enter a text: ")
        if text == "quit":
            break
        try:
            print(countchars(text))
        except:
            print("An error occurred!")