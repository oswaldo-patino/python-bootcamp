import sys
import exercise1, exercise2, exercise3

def main(argv):
    if argv[1] == "exercise1":
        exercise1.run()
    if argv[1] == "exercise2":
        exercise2.run()
    if argv[1] == "exercise3":
        exercise3.run()

if __name__ == "__main__":
    main(sys.argv)