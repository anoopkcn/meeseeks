def strip(list, sep=' '):
    '''returns a list without brakets[]

    For using python list's in other programs

    Arguments:
        a {list} -- one dimensional list

    Example:
    >>> a = [1,2,3,4,5]
    >>> print(strip(a))
    >>> 1 2 4 5
    '''
    return f'{sep}'.join(map(str, list))


def commas(N):
    '''returns a number separated with commas

    Number is returend in a readable format...
    ... with commas separating the digits 

    Arguments:
        N {number} -- a whole number

        Example:
    >>> a = 12345
    >>> print(commas(a))
    >>> 12,345
    '''
    return '{:,}'.format(N)


if __name__ == '__main__':
    # tests
    print(strip([1, 2, 3, 4, 5]))
    print(commas(20000))
