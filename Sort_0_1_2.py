def sort012(arr, n) :
	# write your code here
    # don't return anything 
    i = 0
    mid = 0
    j = n-1
    while mid<=j:
        if arr[mid] == 0:
            arr[mid],arr[i] = arr[i],arr[mid]
            i +=1
            mid +=1
        elif arr[mid] == 1:
            mid +=1
        else:
            arr[mid],arr[j] = arr[j],arr[mid]
            j -=1

arr = [2,2,1,1,0,2,0,1]
print(sort012(arr,len(arr)))
print(arr)