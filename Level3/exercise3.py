from datetime import datetime

def current_age(birth_date: datetime) -> tuple[int, int, int]:
    """
    
    """
    YEAR_DURATION = 365.242 # Constant for year duration in days
    # Get date difference  from today
    dateDiff = (datetime.now() - birth_date).days
    # Get Years
    delta = dateDiff / YEAR_DURATION
    years = int(delta)
    # Get Months
    delta = (delta - years) * 12
    months = int(delta)
    # Get Days
    delta = (delta - months) * YEAR_DURATION / 12
    days = int(delta)
    
    return years, months, days

def run():
    """

    """
    print("##### Exercise 3 #####")
    print("Get the current age")
    while True:
        str = input("Enter your birth date [yyyy-mm-dd] ('quit' for exit): ")
        if str == "quit":
            break
        try:
            age = current_age(datetime.strptime(str, "%Y-%m-%d"))
            print(f"You are {age[0]} years, {age[1]} months and {age[2]} days old")
        except Exception as e:
            print("An error ocurred:", format(e))