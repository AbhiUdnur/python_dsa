def coin_change(arr, N, sum):
    
    arr.sort(reverse=True)

    def solve(n, cap):

        if cap == 0:
            return 1
        
        if n==0:
            return 0
        
        val = arr[n-1]

        if val <= cap:

            c = solve(n, cap-val) + solve(n-1, cap)
            return c
        
        c = 0
        return c
    
    return solve(N, sum)

print(coin_change([1,2,3], 3,4))

# --------------------------------------------------------------------------------------------------

def coin_change(arr, N, sum):
    
    dp = {}
    arr.sort(reverse=True)

    def solve(n, cap):

        if cap == 0:
            return 1
        
        if n==0:
            return 0
        
        if (n,cap) in dp:
            return dp[(n,cap)]

        val = arr[n-1]

        if val <= cap:

            c = solve(n, cap-val) + solve(n-1, cap)
            dp[(n,cap)] = c
            return dp[(n,cap)]
        
        c = 0
        dp[(n,cap)] = c
        return dp[(n,cap)]
    
    return solve(N, sum)

print(coin_change([1,2,3], 3,4))

# --------------------------------------------------------------------------------------------------

def coin_change(arr, N, sum):

    dp = [[0]*(sum+1) for i in range(N+1)]
    arr.sort()
    for i in range(N+1):
        for j in range(sum+1):
            if i == 0:
                dp[i][j] = 0

            if j == 0:
                dp[i][j] = 1
            
            else:
                val = arr[i-1]
                if val <= j:
                    dp[i][j] = dp[i][j-val] + dp[i-1][j]
                
                else:
                    dp[i][j] = 0
    
    return dp[N][sum]
            
print(coin_change([1,2,3], 3,4))
