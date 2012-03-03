def checkInt(i):
    """Checks that the passed variable can have the int() function called on it sucessfully"""
    try:
        int(i)
        return True
    except ValueError:
        return False
