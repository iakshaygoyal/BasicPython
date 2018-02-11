def how_many(dict):
    values=dict.values()
    ans=0
    for l in values:
        ans+=len(l)
    return ans
