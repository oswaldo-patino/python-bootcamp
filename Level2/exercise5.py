def get_args(*args, **kwargs):
    """
    Return the sum of the specified numbers as arguments

    Parameters:
        nums (*int): Numbers 
    """
    print("args:", args)
    print("kwargs:", kwargs)

def run():
    """
    Runs the exercise 5
    """
    print("##### Exercise 5 #####")
    try:
        get_args("test", "args", "values", another="args", which="has", key="words")
    except Exception as e:
        print("An error ocurred:", format(e))