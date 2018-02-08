i=0
n=len(s)
prev_idx=-1
prev_val=-1
max=-1
max_idx=-1

while i<n:
    if i+1>prev_idx:
        j=i+1
    else:
        j=prev_idx

    if 1>prev_val-1:
        val=1
    else:
        val=prev_val-1
    #j=max(i+1, prev_idx)
    #val=max(1, prev_val-1)

    while j<n:
        if(s[j-1:j] <= s[j:j+1]):
            val+=1
        else:
            break
        j+=1

    if(val>max):
        max=val
        max_idx=i

    prev_idx=j
    prev_val=val
    i+=1
    if j==n:
        break

print('Longest substring in alphabetical order is:', s[max_idx : max_idx + max])
