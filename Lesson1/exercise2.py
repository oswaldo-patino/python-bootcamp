def print_reversed(name : str) -> str:
    names = name.lower().split(" ")
    [print(x[::-1].capitalize(), end=" ") for x in names]
    print()

def run():
    print("##### Exercise 2 #####")
    print("Print reversed name. Enter 'quit' to exit.")
    while True:
        first_name = input("First Name: ")
        if first_name == "quit":
            break
        last_name = input("Last Name: ")
        print_reversed("{0} {1}".format(first_name, last_name))