import os
from datetime import datetime

def scan_directory(dir: str):
    """
    Return the information of the given directory

    Parameters:
        dir (str): Directory
    """
    stats = os.stat(dir)
    print("{0:11s} {1:20s} {2:10s} {3:15s} {4:10s} {5:16s} {6:16s} {7:16s}"
        .format("Permissions", "Name", "Size", "Owner", "Device", "Created", "Last modified", "Last accessed"))
    print("{0:11s} {1:20s} {2:10s} {3:15s} {4:10s} {5:16s} {6:16s} {7:16s}"
        .format("-"*11, "-"*20, "-"*10, "-"*15, "-"*10, "-"*16, "-"*16, "-"*16))
    print("{0:11s} {1:20s} {2:10d} {3:15d} {4:10d} {5:16s} {6:16s} {7:16s}"
        .format(oct(stats.st_mode)[-3:],
            os.path.basename(dir), 
            stats.st_size, 
            stats.st_uid, 
            stats.st_dev,
            datetime.fromtimestamp(stats.st_ctime).strftime("%Y-%m-%d %H:%M"),
            datetime.fromtimestamp(stats.st_mtime).strftime("%Y-%m-%d %H:%M"),
            datetime.fromtimestamp(stats.st_atime).strftime("%Y-%m-%d %H:%M")))

def run():
    """
    Runs the exercise 2
    """
    print("##### Exercise 2 #####")
    print("Scans the specified directory. Enter 'quit' to exit.")
    while True:
        dir = input("Enter the directory: ")
        if dir == "quit":
            break
        try:
            scan_directory(dir)
        except Exception as e:
            print("An error ocurred:", format(e))