from decorators import validate_regex

@validate_regex(r"^[a-z]+(?:_[a-z]+)+$")
def validate(*args):
    print("Success!")

def run():
    """

    """
    print("##### Exercise 3 #####")
    print("Decorator to validate a regex.")
    while True:
        text = input("Enter multiple text ('quit' for exit): ")
        if text == "quit":
            break
        try:
            validate(*text.split(" "))
        except Exception as e:
            print("An error ocurred:", format(e))