N=10
def mult (n):
    l = []
    i = 1
    while(i<=n):
        if(n%i==0):
            l.insert(0,(int(n/i),int(n/(n/i))))
        i = i + 1
    return l

print(mult(N))