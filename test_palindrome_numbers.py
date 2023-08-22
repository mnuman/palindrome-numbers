from  palindrome_numbers import *
def test_palindrome_number():
    assert is_palindrome(1), "1 is a palindrome number"
    assert not is_palindrome(12), "12 is not a palindrome number"
    assert is_palindrome(121), "121 is a palindrome number"

def test_reversed_add():
    assert reversed_add(1) == 2
    assert reversed_add(89) == 187
    assert reversed_add(121) == 242
    # test for large number
    assert reversed_add(1_000_000_000_000_000) == 1_000_000_000_000_001

def test_iterate():
    assert iterate(1) == (1,0)
    assert iterate(121) == (121,0)
    assert iterate(12) == (33,1)
    assert iterate(96) == (4884, 4)