def main(s):
    """
    A variable of type str is given. Find how many lowercase letters there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i = 0
    m = 0
    while i<len(s):
        if not s[i] =='o' and not s[i] =='e':
           if not s[i] =='u' and not s[i] =='a':
            if not s[i] =='i' and not s[i] =='y':
              m+=1
        
        i+=1
    return m

v = main("aaaaad")
print(v)