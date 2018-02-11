def biggest(dict):
    values=dict.values()
    ans=0
    for v in values:
        ans=max(ans, len(v))

    return ans
