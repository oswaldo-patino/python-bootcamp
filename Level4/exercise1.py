import re

def regex_letters_joined_with_underscore(text: str) -> bool:
    """
    
    """
    regex = re.compile(r"^[a-z]+(?:_[a-z]+)+$")
    match = bool(regex.search(text))
    return match

def run():
    """

    """
    print("##### Exercise 1 #####")
    print("Regex to find sequences of lowercase letter joined by an underscore.")
    while True:
        text = input("Enter text ('quit' for exit): ")
        if text == "quit":
            break
        try:
            match = regex_letters_joined_with_underscore(text)
            print(f"{text}: {'' if match else 'Not '}Match!")
        except Exception as e:
            print("An error ocurred:", format(e))