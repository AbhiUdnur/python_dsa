def maxTurbulenceSize(arr):
    n = len(arr)
    dp = 0 
    ans = 0 
        
    for i in range(n):
        if i==0:
            dp = 1 
        elif i==1:
            if arr[i]!=arr[i-1]:
                dp = 2 
            else:
                dp = 1 
        else:
            if (arr[i]>arr[i-1] and arr[i-1]<arr[i-2]) or (arr[i]<arr[i-1] and arr[i-1]>arr[i-2]):
                dp = 1+dp
            else:
                if arr[i]!=arr[i-1]:
                    dp = 2 
                else:
                    dp = 1
        ans = max(ans,dp)
                        
    return ans

print(maxTurbulenceSize([9,4,2,10,7,8,8,1,9]))
