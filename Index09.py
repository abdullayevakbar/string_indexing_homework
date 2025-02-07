def main(s):
    """
    a single character string is given. Convert it to int type, return -1 if not possible.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    if(s[0] < 0 or s[0] > '9'):
        return -1
    return int(s)
