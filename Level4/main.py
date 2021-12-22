import sys
import exercise1, exercise3

def main(argv, option = 0):
    arg = ""
    if len(argv) > 1:
        arg = argv[1]

    if arg == "exercise1" or option == 1:
        exercise1.run()
    elif arg == "exercise3" or option == 3:
        exercise3.run()

if __name__ == "__main__":
    while True:
        print("""
***** Level 4 *****
Enter an option to continue:
1 or 3: Exercise
0: Exit
            """)
        try:
            option = int(input())
            if option == 1 or option == 3:
                main(sys.argv, option)
            elif option == 0:
                break
            else:
                print(f"Invalid input: {option}. Option 1 or 3")
        except Exception as e:
            print(f"Invalid input: {e}. Please try again.")
