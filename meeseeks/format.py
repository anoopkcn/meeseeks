def to_string(list, sep=" "):
    """returns a list without brakets[]

    For using python list's in other programs

    Arguments:
        a {list} -- one dimensional list

    Example:
    >>> a = [1,2,3,4,5]
    >>> print(strip(a))
    >>> 1 2 4 5
    """
    return f"{sep}".join(map(str, list))


def with_commas(N):
    """returns a number separated with commas

    Number is returend in a readable format...
    ... with commas separating the digits 

    Arguments:
        N {number} -- a whole number

        Example:
    >>> a = 12345
    >>> print(commas(a))
    >>> 12,345
    """
    return "{:,}".format(N)


def is_number(s):
    """
    Check if a string can be cast to a float or numeric (integer).
    Takes a string.
    Returns True or False
    """
    try:
        float(s)
        return True
    except ValueError:
        pass
    try:
        import unicodedata

        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
    return False


def to_number(s):
    """
    Cast a string to a float or integer. 
    Tries casting to float first and if that works then it tries casting the 
    string to an integer.
    Returns a float, int, or if fails, False. (Where using, it shouldn't ever
    trigger returning `False` because checked all could be converted first.)
    """
    try:
        number = float(s)
        try:
            number = int(s)
            return number
        except ValueError:
            pass
        return number
    except ValueError:
        pass
    try:
        import unicodedata

        num = unicodedata.numeric(s)
        return num
    except (TypeError, ValueError):
        pass
    return False


if __name__ == "__main__":
    # tests
    print(to_string([1, 2, 3, 4, 5]))
    print(with_commas(20000))
    print(is_number("3e-4"))
    print(to_number("3.12e2"))
