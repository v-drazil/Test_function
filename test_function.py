from os import urandom
import pytest


def abc_random_string(length):
    '''Return abc + random string'''

    if length < 1:
        raise ValueError("{} is not valid value".format(length))
    
    return 'abc' + str(urandom(length))


def is_prime(number):
    """Return True if *number* is prime."""

    if number < 2:
        raise ValueError("{} is not valid value".format(number))
    
    for element in range(2,number):
        if (number % element) == 0:
            return False
    return True


def print_next_prime(number):
    """Print the closest prime number larger than *number*."""

    if number < 1:
        raise ValueError("{} is not valid value".format(number))

    index = number
    while True:
        index += 1
        if is_prime(index):
            print(index)
            return(index)


def test_abc_random_string():
    assert type(abc_random_string(1)) == str


def test_abc_random_string2():
    assert abc_random_string(1).startswith("abc")


def test_abc_random_string3():
    assert len(abc_random_string(1)) > 3
    

def test_abc_random_string4():
    with pytest.raises(ValueError):
        abc_random_string(0)

        
def test_is_prime():
    assert is_prime(11) is True


def test_is_prime2():
    assert is_prime(12) is False


def test_is_prime3():
    with pytest.raises(ValueError):
        is_prime(-1)
    

def test_print_next_prime():
    assert print_next_prime(11) == 13


def test_print_next_prime2():
    assert print_next_prime(3) > 3


def test_print_next_prime3():
    with pytest.raises(ValueError):
        print_next_prime(0)
