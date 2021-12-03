class Error(Exception):
    """
    Base class for other exceptions
    """
    pass
class FormulaError(Error):
    """
    Exception raised for errors in the formula inputs
    Attributes:
        expression -- formula expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

    def __str__(self) -> str:
        return f"{self.expression} -> {self.message}"

def calculate(operation: str) -> float:
    """
    Runs the command int the native OS

    Parameters:
        dir (str): Directory
    """
    operators = ("+", "-", "*", "/")
    inputs = operation.split(" ")
    if len(inputs) != 3:
        raise FormulaError(operation, "Wrong number of parameters")

    x1 = 0.0
    x2 = 0.0
    operator = inputs[1]
    result = 0.0

    try:
        x1 = float(inputs[0])
    except ValueError as e:
        raise FormulaError(x1, f"Invalid value for operation {e.args}")
        
    try:
        x2 = float(inputs[2])
    except ValueError as e:
        raise FormulaError(x2, f"Invalid values for operation {e.args}")
    
    if operator not in operators:
        raise FormulaError(operator, f"Invalid operator. Only {operators} operators allowed")

    try:
        if operator == "+":
            result = x1 + x2
        elif operator == "-":
            result = x1 - x2
        elif operator == "*":
            result = x1 * x2
        elif operator == "/":
            result = x1 / x2
    except Exception as e:
        raise FormulaError(operation, f"Invalid operation {e.args}")

    return result

def run():
    """
    Runs the Project - Simple Calculator
    """
    print("##### Project - Simple Calculator #####")
    while True:
        operation = input("Enter the operation ('quit' for exit): ")
        if operation == "quit":
            break
        try:
            print("Result =", calculate(operation))
        except Exception as e:
            print(f"{type(e)}: {str(e)}")