"""
>>> sum(2, 3)
4

>>> sum(2, 3)
5
"""
def sum(a, b):
    return a + b


if __name__ == "__main__":
    import doctest
    doctest.testmod()