import sys
import exercise1, exercise2, exercise3, exercise4, exercise5, exercise6

def main(argv, option = 0):
    arg = ""
    if len(argv) > 1:
        arg = argv[1]

    if arg == "exercise1" or option == 1:
        exercise1.run()
    elif arg == "exercise2" or option == 2:
        exercise2.run()
    elif arg == "exercise3" or option == 3:
        exercise3.run()
    elif arg == "exercise4" or option == 4:
        exercise4.run()
    elif arg == "exercise5" or option == 5:
        exercise5.run()
    elif arg == "exercise6" or option == 6:
        exercise6.run()

if __name__ == "__main__":
    while True:
        print("""
***** Level 3 *****
Enter an option to continue:
1-6: Exercises
0: Exit
            """)
        try:
            option = int(input())
            if option >= 1 and option <= 6:
                main(sys.argv, option)
            elif option == 0:
                break
            else:
                print(f"Invalid input: {option}. Option between 1-6")
        except Exception as e:
            print(f"Invalid input: {e}. Please try again.")
