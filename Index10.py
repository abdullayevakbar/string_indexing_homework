def main(s):
    """
    A string of five numbers is given. Find the sum of its numbers.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    x = 0
    if(s[0] >= '0' and s[0] <= '9'):
        x += (s[0]-'0')
    if(s[1] >= '0' and s[1] <= '9'):
        x += (s[1]-'0')
    if(s[2] >= '0' and s[2] <= '9'):
        x += (s[2]-'0')
    if(s[3] >= '0' and s[3] <= '9'):
        x += (s[3]-'0')
    if(s[4] >= '0' and s[4] <= '9'):
        x += (s[4]-'0')
    return x
