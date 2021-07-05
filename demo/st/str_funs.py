def hasdigit(s):
    for c in s:
        if c.isdigit():
            return True

    return False


def getwords(s):
    return s.split()
