def recurPower(base, exp):
    if exp==0:
        return 1

    ans=base*recurPower(base,exp-1)
    return ans
