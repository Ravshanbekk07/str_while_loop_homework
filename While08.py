def main(s):
    """
    A string of numbers is given. Find how many odd digits there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i = 0
    odds = 0
    while i<len(s):
        if int(s[i])%2 !=0:
            odds+=1
        i+=1
    return odds

v = main("3489769")
print(v)