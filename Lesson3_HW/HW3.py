def init(sp):
    result = {}
    st = sp
    st = st.lower()
    st = st.replace(",","")
    st = st.split(" ")
    for i in st:
        if(len(result.items())!=0):
            flag = True
            for a,b in result.items():
                if(i==a):
                    result[a] += 1
                    flag = False
            if(flag == True):
                result[i] = 1
        else:
            result[i] = 1
    
    return result


sp = 'a aa abC aa ac, abc bcd a'

for a,b in init(sp).items():
    print(f'{a}: {b};',end= ' ')