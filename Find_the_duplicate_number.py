def findDuplicate(arr:list, n:int):
    # Write your code here.
    # Returns an integer.
    for i in range(n):
        ind = abs(arr[i]) - 1
        if arr[ind] < 0:
            return abs(arr[i])
        arr[ind] = -arr[ind]


arr = [1,3,4,2,2]
print(findDuplicate(arr,len(arr)))