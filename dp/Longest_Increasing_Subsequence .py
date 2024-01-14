def lon_Ss(arr, n, li=-1):

    if n==0:
        return 0
    
    if li==-1 or arr[n-1] < arr[li]:

        return max(1+lon_Ss(arr, n-1,n-1),lon_Ss(arr, n-1, li))
    
    return lon_Ss(arr, n-1, li)

print(lon_Ss([0,4,6,1,2,5,3,5,7,8], 10))

# ------------------------------------------------------------------------

def lon_Ss(arr,n):

    dp = [0] * n
    dp[0] = 1

    for i in range(1,n):
    
        j = i-1
        ce = arr[i]
        mx = 0
    
        while j >=0:
    
            if arr[j]<ce:
                mx = max(mx, dp[j])
    
            j-=1
        
        dp[i] = 1+mx
    
    return max(dp)

print(lon_Ss([0,4,6,1,2,5,3,5,7,8], 10))