def main(s):
    """
    A variable of type str is given. Find how many uppercase letters there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i = 0
    m = 0
    while i<len(s):
        if s[i].istitle():
            m+=1
        i+=1
    return m

v = main("CodeSchoolUz")
print(v)