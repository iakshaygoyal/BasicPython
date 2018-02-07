n=int(input('Please think of a number between 0 and 100! '))
low=0
high=100
ans=(low+high)//2

while low<high:
    print('Is your secret number '+str(ans)+'?')
    reply=input()

    if reply=='h':
        high=ans
    elif reply=='l':
        low=ans
    elif reply=='c':
        break
    else:
        print('Sorry, I did not understand your input.')
        continue
    ans=(low+high)//2

print('Game over. Your secret number was: '+str(ans))
