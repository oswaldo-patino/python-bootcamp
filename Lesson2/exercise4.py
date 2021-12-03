def sum_args(*nums: int) -> int:
    """
    Return the sum of the specified numbers as arguments

    Parameters:
        nums (*int): Numbers

    Returns:
        result (int): Sum of the arguments
    """
    result = sum(nums)
    return result

def run():
    """
    Runs the exercise 4
    """
    print("##### Exercise 4 #####")
    print("Enter some numbers to get the sum. Enter 'quit' to exit.")
    while True:
        nums = input("Numbers: ").split(" ")
        if nums[0] == "quit":
            break
        try:
            nums = [int(x) for x in nums]
            print("Sum =", sum_args(*nums))
        except Exception as e:
            print("An error ocurred:", format(e))