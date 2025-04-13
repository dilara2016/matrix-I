x = [[7,1],
     [9,3]]

y = [[2,4],
     [5,5]]

eList = [[0,0],
         [0,0]]

for i in range(len(x)):
    for j in range(len(y[0])):
        for k in range(len(y)):
            eList[i][j] += x[i][k] * y[k][j]
for l in eList:
    print(l)