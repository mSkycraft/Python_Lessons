list_math = [3,('Спартак',9,'Зенит',10),('Локомотив',12,'Зенит',3),('Спартак',8,'Локомотив',15)]

def PrintDict(dict):
    for i,j in dict.items():
        print(i , j)

def Result_table(lst:list):
    matrix = {}
    del lst[0]
    for i in (0,2):
        for score in lst:
            if not(score[i] in matrix):
                matrix[score[i]]= [1,0,0,0,0]
            else:
                matrix[score[i]][0] += 1
            if(score[i+1]>score[i-1]):
                matrix[score[i]][1] += 1
                matrix[score[i]][4] += 3
            elif(score[i+1]<score[i-1]):
                matrix[score[i]][3] += 1
            elif(score[i+1]==score[i-1]):
                matrix[score[i]][3] += 1
                matrix[score[i]][3] += 1
    return matrix

PrintDict(Result_table(list_math))