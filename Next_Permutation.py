def swapTwoElement(idx1,idx2,arr):
    arr[idx1],arr[idx2] = arr[idx2],arr[idx1]

def reverse(arr):
    arr.sort()

def swapAllElementAfterIndex(idx,arr):
    i = idx+1
    j = len(arr)-1
    while i<j:
        arr[i],arr[j] = arr[j],arr[i]
        i+=1
        j-=1

def nextPermutation(permutation, n):
    # Write your code here.
    # Return a list.
    arr = permutation
    idx = -1
    for i in range(n-1,0,-1):
        if arr[i] > arr[i-1]:
            idx = i-1
            break
    if idx == -1:
        reverse(arr)
    else:
        for i in range(n-1,idx,-1):
            if arr[idx] < arr[i]:
                swapTwoElement(idx,i,arr)
                break
        swapAllElementAfterIndex(idx,arr)
    return arr

permutation = [1,2,3,4]
print(nextPermutation(permutation,4))