def is_vowel(letter : str) -> bool:
    """
    Returns if a letter is a vowel

    Parameters:
        letter (str): A character of a string.

    Returns:
        result (bool): True if is a vowel, False otherwise.
    """
    result = letter.lower() in ["a", "e", "i", "o", "u"]
    return result

def run():
    """
    Runs the exercise 1
    """
    print("##### Exercise 1 #####")
    print("Check if a letter is a vowel. Enter 'quit' to exit.")
    while True:
        letter = input("Letter: ")
        if letter == "quit":
            break
        print("{0} {1} a vowel".format(letter, "is" if is_vowel(letter) else "is not"))