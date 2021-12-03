import os

def run_cmd(command: str):
    """
    Runs the command int the native OS

    Parameters:
        dir (str): Directory
    """
    os.system(command)

def run():
    """
    Runs the exercise 3
    """
    print("##### Exercise 3 #####")
    print("Runs the specified command. Enter 'quit' to exit.")
    while True:
        command = input("Enter the command: ")
        if command == "quit":
            break
        try:
            run_cmd(command)
        except Exception as e:
            print("An error ocurred:", format(e))