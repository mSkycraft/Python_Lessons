def pi(d):
    if(d>=1): D = 0
    else: D = 1
    while(d*10<1):
        d = d*10
        D = D + 1
    sum = 0
    for i in range(D):
        sum = sum + 1/(16**i)*(4/(8*i+1)-2/(8*i+4)-1/(8*i+5)-1/(8*i+6))
    print(sum)    
    return round(sum,D)

d = 0.001
print(pi(d))