def remove_duplicates(aList : list) -> list:
    """
    Returns a list without duplicates

    Parameters:
        aList (list): A list.

    Returns:
        result (list): The given list without duplicates.
    """
    result = list(dict.fromkeys(aList))
    return result

def run():
    """
    Runs the exercise 7
    """
    print("##### Exercise 7 #####")
    aList = [1, 1, 2, 3, 5, 3, 7]
    print(aList)
    aList = remove_duplicates(aList)
    print(aList)