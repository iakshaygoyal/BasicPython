def isIn(char, aStr):
    low=0
    high=len(aStr)-1
    while low<=high:
        idx = (low + high) // 2
        if aStr[idx]==char:
            return True
        elif aStr[idx]>char:
            high=idx-1
        else:
            low=idx+1

    return False
