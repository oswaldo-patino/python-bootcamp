class Test:
    def __init__(self) -> None:
        self.list = []
    
    def add(self, item: int) -> int:
        self.list.append(item)
        return item

    def add(self, *items: int):
        self.list += items

    def get_sorted(self) -> list[int]:
        return sorted(self.list)

    def __str__(self) -> str:
        return self.list.__str__()

def run():
    """

    """
    print("##### Exercise 6 #####")
    print("Test Class")
    try:
        test = Test()
        print(f"Initial list: {test}")
        test.add(1)
        print(f"Adding 1: {test}")
        test.add(5, 4, 3, 2)
        print(f"Adding more numbers: {test}")
        print(f"Sorted: {test.get_sorted()}")
    except Exception as e:
        print("An error ocurred:", format(e))