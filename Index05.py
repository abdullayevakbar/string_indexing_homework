def main(s):
    """
    Given a variable s string of length five. Determine the number of digits involved in this variable.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    x = 0
    if s[0] >= '0' and s[0] <= '9':
        x += 1
    if s[2] >= '0' and s[2] <= '9':
        x += 1
    if s[3] >= '0' and s[3] <= '9':
        x += 1
    if s[4] >= '0' and s[4] <= '9':
        x += 1
    if s[1] >= '0' and s[1] <= '9':
        x += 1

    return x
