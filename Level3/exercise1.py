def count_str2(lst: list[str]) -> int:
    """
    
    """
    result = sum([len(x) > 2 for x in lst])
    return result

def run():
    """

    """
    print("##### Exercise 1 #####")
    print("Count strings length greater than 2.")
    while True:
        str = input("Enter strings ('quit' for exit): ")
        if str == "quit":
            break
        try:
            count = count_str2(str.split(" "))
            print(f"Number of strings with 2 or more characters: {count}")
        except Exception as e:
            print("An error ocurred:", format(e))