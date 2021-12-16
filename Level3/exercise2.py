from datetime import datetime

def current_date() -> str:
    """
    
    """
    result = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return result

def run():
    """

    """
    print("##### Exercise 2 #####")
    print("Current date and time:")
    print(current_date)