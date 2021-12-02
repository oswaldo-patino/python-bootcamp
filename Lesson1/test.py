import sys
import os
import exercise1, exercise2, exercise3, exercise4, exercise5
import exercise6, exercise7, exercise8, exercise9, exercise10

def main(argv):
    if argv[1] == "exercise1":
        exercise1.run()
    elif argv[1] == "exercise2":
        exercise2.run()
    elif argv[1] == "exercise3":
        exercise3.run()
    elif argv[1] == "exercise4":
        exercise4.run()
    elif argv[1] == "exercise5":
        exercise5.run()
    elif argv[1] == "exercise6":
        exercise6.run()
    elif argv[1] == "exercise7":
        exercise7.run()
    elif argv[1] == "exercise8":
        exercise8.run()
    elif argv[1] == "exercise9":
        exercise9.run()
    elif argv[1] == "exercise10":
        exercise10.run()

if __name__ == "__main__":
    main(sys.argv)