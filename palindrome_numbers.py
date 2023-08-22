"""
From a column by Martin Gardner in Scientific American, reproduced "The Colossal Book of Mathematics"
by Martin Gardner, ISBN  9780393020236.
"""
# sys.set_int_max_str_digits(20000)     # no longer needed - 1,000 iterations does not cause the conversion to exceed the limit
MAX_ITERATIONS = 1_000                  # max number of iterations to consider
no_palindrome = []                      # collect numbers that cannot be resolved to a palindrome number

def is_palindrome(number: int) -> bool:
    s = str(number)
    return s == s[::-1]


def reversed_add(number: int) -> int:
    """
    Given a number, reverse its digits and add to itself
    """
    return int(str(number)[::-1]) + number

def iterate(number: int) -> (int,int):
    """
    Iterate until the number is a palindrome number. If it is currently
    not a palindrome number, add its reversed number to it.
    """
    iterations = 0
    while not is_palindrome(number) and iterations < MAX_ITERATIONS:
        iterations += 1
        number = reversed_add(number)
    return (number, iterations) if iterations < MAX_ITERATIONS else (None, None)

if __name__ == "__main__":
    for i in range(1,10000):
        palindrome, iters = iterate(i)
        if palindrome is not None:
            print(f"Number {i} yields palindrome {palindrome} after {iters} iterations")
        else:
            no_palindrome.append(i)
    print(f"No palindrome could be found within {MAX_ITERATIONS} for {no_palindrome}")
