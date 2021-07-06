def hasdigit(s):
    """
    Function returns true if given string has any digit anywhere.

    :param s: string which is to be tested
    :return : True if string has a digit otherwise false
    """
    for c in s:
        if c.isdigit():
            return True

    return False


def getwords(s):
    return s.split()
