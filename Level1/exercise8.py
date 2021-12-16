def remove_item_at(aTuple : tuple, index : int) -> tuple:
    """
    Returns a tuple with the item removed by the given index

    Parameters:
        aTuple (tuple): A tuple.

    Returns:
        result (tuple): The given tuple without the item by the specified index.
    """
    result = aTuple[:index] + aTuple[index+1:]
    return result

def run():
    """
    Runs the exercise 8
    """
    print("##### Exercise 8 #####")
    aTuple = (1, 1, 2, 3, 5, 3, 7)
    print(aTuple)
    aTuple = remove_item_at(aTuple, 4)
    print("After removing index 4:", aTuple)