import json

def print_json(filename: str):
    """

    """
    data = {}
    with open(filename, "r") as file:
        data = json.load(file)
    str = json.dumps(data, indent=4)
    print(str)
    return data

def sort_json(filename: str):
    """
    
    """
    data = print_json(filename)
    with open(filename, "w") as file:
        json.dump(data, file, indent=4, sort_keys=True)
    return data

def run():
    """

    """
    print("##### Exercise 5 #####")
    print("Sort JSON by keys.")
    while True:
        filename = input("Enter JSON file name ('quit' for exit): ")
        if filename == "quit":
            break
        try:
            sort_json(filename)
            print("--------SORTED--------")
            print_json(filename)
        except Exception as e:
            print("An error ocurred:", format(e))