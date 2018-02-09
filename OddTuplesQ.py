def oddTuples(t):
    new_t=()
    for i in range(len(t)):
        if i%2==0:
            new_t=new_t+(t[i],)

    return new_t
