def count_str3(lst: list[str]) -> list:
    """
    
    """
    result = [len(x) if len(x) >= 3 else "x" for x in lst]
    return result

def run():
    """

    """
    print("##### Exercise 4 #####")
    print("Print strings length if greater than 3.")
    while True:
        str = input("Enter strings ('quit' for exit): ")
        if str == "quit":
            break
        try:
            lst = count_str3(str.split(" "))
            print(f"Length of strings with 3 or more characters: {lst}")
        except Exception as e:
            print("An error ocurred:", format(e))