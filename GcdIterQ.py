def gcdIter(a, b):
    n=min(a,b)
    while(n>1):
        if a%n==0 and b%n==0:
            return n
        n-=1

    return n
