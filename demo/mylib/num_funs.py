# Module with function related to numbers

def isodd(n):
    return n % 2 == 1


def ispositive(n):
    return n > 0


# Execute code only when module is run as script
if __name__ == '__main__':
    print(isodd(11), isodd(10))
    print(ispositive(11), ispositive(-10))
