import sys
import exercise1, exercise2, exercise3, exercise4, exercise5
import calculator

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
    elif argv[1] == "calculator":
        calculator.run()

if __name__ == "__main__":
    main(sys.argv)