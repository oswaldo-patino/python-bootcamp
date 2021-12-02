def merge_dictionaries(dict1: dict, dict2: dict) -> dict:
    """
    Returns a merged dictionary

    Parameters:
        dict1 (dict): A dictionary.
        dict2 (dict): A dictionary.

    Returns:
        result (dict): The merged dictionary.
    """
    result = {**dict1, **dict2}
    return result

def run():
    """
    Runs the exercise 8
    """
    print("##### Exercise 8 #####")
    dict1 = {"a": 1, "b": 2, "c": 3}
    dict2 = {"c": 1, "d": 2, "e": 3}
    print(dict1)
    print(dict2)
    result = merge_dictionaries(dict1, dict2)
    print(result)