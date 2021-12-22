g_list = []
    
def add(item: int) -> int:
    global g_list
    g_list.append(item)
    return item

def add(*items: int):
    global g_list
    g_list += items

def get_sorted() -> list[int]:
    global g_list
    return sorted(g_list)

def run():
    """

    """
    print("##### Exercise 6 #####")
    print("Test Class")
    try:
        print(f"Initial list: {g_list}")
        add(1)
        print(f"Adding 1: {g_list}")
        add(5, 4, 3, 2)
        print(f"Adding more numbers: {g_list}")
        print(f"Sorted: {get_sorted()}")
    except Exception as e:
        print("An error ocurred:", format(e))