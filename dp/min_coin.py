def min_coin(arr, amount):

    N = len(arr)
    arr.sort(reverse=True)
    dp = {}
    def solve(n, amt):

        if amt == 0:
            return 0
        
        if n == 0:
            return float("INF")
        
        if (n, amt) in dp:
            return dp[(n, amt)]

        val = arr[n-1]
        
        if val<= amt:

            dp[(n, amt)] = min(1+solve(n, amt-val), solve(n-1, amt))
            return dp[(n, amt)]
        
        dp[(n, amt)] = float("INF")
        return dp[(n, amt)]
    
    val = solve(N, amount)
    
    if val >= 10**9+7:
        return -1
    
    return val

print(min_coin([1,2,5], 11))

# --------------------------------------------------------------------------------------------------

def min_coin(arr, amount):

    N = len(arr)
    arr.sort()
    dp = {}
    def solve(amt):

        if amt == 0:
            return 0
        
        if amt in dp:
            return dp[amt]
        
        ans = float("INF")

        for coin in arr:
            if coin<=amt:
                ans = min(ans, 1+solve(amt-coin))

            else:
                break
        
        dp[amt] = ans
        return ans
    
    val = solve(amount)

    if val > 10**9 + 7:
        return -1
    
    return val

print(min_coin([1,2,5], 11))

# -----------------------------------------------------------------------------------------------------------------

def min_coin(arr, amount):

    N = len(arr)
    arr.sort()
    dp = [0]*(amount+1)
    
    for amt in range(1,amount+1):
        ans = float("INF")
        for coin in arr:
            if coin <= amt:
                ans = min(ans, 1+dp[amt-coin])
            
            else:
                break

        dp[amt] = ans
    
    if dp[amount]>=10**9+7:
        return -1
    
    return dp[amount]

print(min_coin([1,2,5], 6))



    
