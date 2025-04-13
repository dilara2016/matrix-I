x = [[4,3],
     [6,2]]
y = [[8,4],
     [1,3]]

eList = [[0,0],
         [0,0]]


for i in range(len(x)):
    for j in range(len(y)):
        eList[i][j] = x[i][j] - y[i][j]

for m in eList:
    print(m)