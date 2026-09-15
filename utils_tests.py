from utils import utils

def reversed_test():
    """ Test the reversed function. """

    assert utils.reversed(123) == 321
    print("Test passed for input 123")

    assert utils.reversed(str(456)) == 654
    print("Test passed for input '456'")

    assert utils.reversed(float(789.0)) == 987
    print("Test passed for input 789.0")

    assert utils.reversed(0) == 0
    print("Test passed for input 0")

    assert utils.reversed(-321) == -123
    print("Test passed for input -321")

    # testing Exceptions for invalid inputs
    try:
        utils.reversed("not_a_number")
    except TypeError:
        pass  # Test passes
    print("Test passed for input 'not_a_number'")

    
    try:
        utils.reversed(None)
    except TypeError:
        pass  # Test passes
    print("Test passed for input None")

    try:
        utils.reversed(float(78.9))
    except TypeError:
        pass  # Test passes
    print("Test passed for input 78.9")

    return "All tests passed for reversed function."

def formatter_test():
    """ Test the formatter function. """

    assert utils.formatter(10) == ('0b1010', '0o12')
    print("Test passed for input 10")

    assert utils.formatter(str(255)) == ('0b11111111', '0o377')
    print("Test passed for input '255'")

    assert utils.formatter(float(100.0)) == ('0b1100100', '0o144')
    print("Test passed for input 100.0")

    assert utils.formatter(0) == ('0b0', '0o0')
    print("Test passed for input 0")

    assert utils.formatter(-5) == ('-0b101', '-0o5')
    print("Test passed for input -5")

    # testing Exceptions for invalid inputs
    try: 
        utils.formatter("not_a_number")
    except TypeError:
        pass  # Test passes
    print("Test passed for input 'not_a_number'")

    try:
        utils.formatter(None)
    except TypeError:
        pass  # Test passes
    print("Test passed for input None")

    try:
        utils.formatter(float(78.9))
    except TypeError:
        pass  # Test passes
    print("Test passed for input 78.9")

    return "All tests passed for formatter function."

if __name__ == "__main__":
    print(reversed_test())
    print(formatter_test())