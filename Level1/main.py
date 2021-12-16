import sys
import exercise1, exercise2, exercise3, exercise4, exercise5
import exercise6, exercise7, exercise8, exercise9, exercise10

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
    elif arg == "exercise7" or option == 7:
        exercise7.run()
    elif arg == "exercise8" or option == 8:
        exercise8.run()
    elif arg == "exercise9" or option == 9:
        exercise9.run()
    elif arg == "exercise10" or option == 10:
        exercise10.run()

if __name__ == "__main__":
    while True:
        print("""
***** Level 1 *****
Enter an option to continue:
1-10: Exercises
0: Exit
            """)
        try:
            option = int(input())
            if option >= 1 and option <= 10:
                main(sys.argv, option)
            elif option == 0:
                break
            else:
                print(f"Invalid input: {option}. Option between 1-10")
        except Exception as e:
            print(f"Invalid input: {e}. Please try again.")
