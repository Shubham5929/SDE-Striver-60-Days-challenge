def maxSubarraySum(arr, n) :

	# Your code here
    # return the answer
        maxi = 0
        temp = 0
        for i in range(n):
            if (temp + arr[i]) <0:
                temp = 0
            else:
                temp += arr[i]
            maxi = max(temp,maxi)
        return maxi 

arr = [20,-30,24,40]
n = len(arr)
print(maxSubarraySum(arr,n))