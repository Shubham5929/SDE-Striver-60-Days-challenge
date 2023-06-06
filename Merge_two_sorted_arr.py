def ninjaAndSortedArrays(arr1,arr2,m,n):
    temp = m+n-1
    i = m-1
    j = n-1
    while i>=0 and j>=0:
        if arr1[i] > arr2[j]:
            arr1[temp] = arr1[i]
            i -=1
        else:

            arr1[temp] = arr2[j]
            j -=1
        temp -=1
    if i<0 and j>=0:
        while j>=0:
            arr1[temp] = arr2[j]
            j-=1
            temp -=1
    return arr1

# arr1 = [3,6,9,0,0]
# arr2 = [4,10]

arr1 = [3,4,6,0,0,0]
arr2 = [1,8,10]

print(ninjaAndSortedArrays(arr1,arr2,len(arr1)-len(arr2),len(arr2)))