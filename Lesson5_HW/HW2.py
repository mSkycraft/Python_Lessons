mas = [1, 5, 2, 3, 4, 4, 9, 1, 7]

def sort(m):
    for i in range(len(m)):
        for j in range(len(m)-1):
            if(m[j]>m[j+1]):
                tmp = m[j]
                m[j] = m[j+1]
                m[j+1] = tmp
    return m


def findrange(m):
    flag = False
    curr = m[0]
    result = '['+ str(m[0])+','
    for i in range(1,len(m)):
        print(m[i]-curr)
        if(m[i]-curr != 1):
            result += str(m[i-1]) + ' ]'
            flag = True
            break
        curr = m[i]
    if(flag == False):
        result += str(m[len(m)-1]) + ' ]'
    return result



mas = sort(mas)
print(mas)
print(list(set(mas)))
print(findrange(list(set(mas))))

