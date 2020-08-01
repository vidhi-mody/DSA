def find_ugly_number(n):
    if(n==1):
        return 1
    i1 = 0
    i2 = 0
    i3 = 0
    ugly_number = [1]
    while(n>1):
        ans = min(ugly_number[i1]*2, ugly_number[i2]*3, ugly_number[i3]*5)
        if(ans==ugly_number[i1]*2):
            i1 = i1 + 1
        if(ans==ugly_number[i2]*3):
            i2 = i2 + 1
        if(ans==ugly_number[i3]*5):
            i3 = i3 + 1
        n = n - 1
        ugly_number.append(ans)

    return ugly_number[-1]

answer = find_ugly_number(150)
print(answer)

