def max_subarray(arr):
    
    dp = [0]*len(arr)
    dp[0] = arr[0]

    for i in range(1,len(arr)):

        dp[i] = max(arr[i], dp[i-1]+arr[i])

    return max(dp)

print(max_subarray([-2,1,-3,4,-1,2,1,-5,4]))

# -----------------------------------------------------------------------

def max_subarray(arr):

    temp = arr[0]
    mx = arr[0]

    for i in range(1,len(arr)):

        temp = max(arr[i], temp+arr[i])
        mx = max(temp, mx)

    return mx

print(max_subarray([-2,1,-3,4,-1,2,1,-5,4]))
