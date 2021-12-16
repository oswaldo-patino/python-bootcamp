from decorators import validate_regex

@validate_regex(r"^[a-z]+_[a-z]+$")
def test(text):
    print(text)
