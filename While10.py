def main(s):
    """
    A string of numbers is given. Find and return the sum of all odd digits.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i = 0
   
    sum_of_odds  = 0
    while i<len(s):
        if int(s[i])%2 !=0:
            
             sum_of_odds+=int(s[i])
        i+=1
    return sum_of_odds

v = main("98421")
print(v)