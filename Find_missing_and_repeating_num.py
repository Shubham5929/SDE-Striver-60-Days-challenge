def missingAndRepeating(arr, n):
    # Write your code here
    totalSumWithDup = sum(arr)
    totalSum = (n*(n+1))/2

    for i in range(n):
        ind = abs(arr[i]) - 1
        if arr[ind] < 0:
            rep_num = abs(arr[i])
            break
        arr[ind] = -arr[ind]
    missingNum = totalSum - (totalSumWithDup - rep_num)
    return [int(missingNum),rep_num]


arr = [1,2,1,3,4]
print(missingAndRepeating(arr,len(arr)))
