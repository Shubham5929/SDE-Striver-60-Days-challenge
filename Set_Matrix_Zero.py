def setZeros(matrix):
    c = True 
    row = len(matrix)
    col = len(matrix[0])

    for i in range(row):
        if matrix[i][0] == 0:
            c = False
        for j in range(1,col):        
            if matrix[i][j] == 0:
                matrix[i][0],matrix[0][j] = 0,0
        

    for i in range(row-1,-1,-1):
        for j in range(col-1,0,-1):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
        
        if c == False:
            matrix[i][0] = 0

# matrix = [[7,19,3],[4,21,0]]
matrix = [[1,2,3],[4,0,6],[7,8,9]]
setZeros(matrix)
print(matrix)

