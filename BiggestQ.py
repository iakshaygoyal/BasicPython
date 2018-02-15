def biggest(dict):
    items=dict.items()
    max=-1
    ans=None
    for i in items:
        if len(i[1]) > max:
            max=len(i[1])
            ans=i[0]

    return ans
