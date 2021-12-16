import re
import functools

def evaluate_regex(text: str, regex: str) -> bool:
    """
    
    """
    regex = re.compile(regex)
    match = bool(regex.search(text))
    return match

def validate_regex(regex):
    """

    """
    def decorator_validate_regex(func):
        @functools.wraps(func)
        def wrapper_validate_regex(*args, **kwargs):
            match = False
            for arg in args:
                match = evaluate_regex(arg, regex)
                return match
            return func(args, kwargs)
        return wrapper_validate_regex
    return decorator_validate_regex