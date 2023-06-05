def printPascal(n:int):
    # Write your code here.
    # Return a list of lists.
    t1 = [[1]]
    for i in range(1,n):
        x1 = [1]
        if i>1:
            for j in range(i-1):
                print(x1,i-1,j)
                x1.append(t1[i-1][j]+t1[i-1][j+1])
        x1.append(1)
        t1.append(x1)
    return t1

print(printPascal(6))