def knapsack_unbounded(W,N, val, wt):
    def helper(n, cap):

        if n==0 or cap == 0:
            return 0
        
        cwt = wt[n-1]
        cv = val[n-1]

        if cwt <= cap:
            c1 = cv+helper(n, cap-cwt)
            c2 = helper(n-1, cap)
            return max(c1, c2)

        return helper(n-1, cap)
    
    return helper(N, W)

print(knapsack_unbounded(3,2,[1,1], [2,1]))

# ---------------------------------------------------------------- top-down/ memoisation ----------------------------------------------------

def knapsack_unbounded(W,N, val, wt):
    def helper(n, cap):
        
        dp = {}
        
        if n==0 or cap == 0:
            return 0
        
        if (n,cap) in dp:
            return dp[(n,cap)]
        
        cwt = wt[n-1]
        cv = val[n-1]

        if cwt <= cap:
            
            c1 = cv+helper(n, cap-cwt)
            c2 = helper(n-1, cap)

            dp[(n,cap)] = max(c1, c2)
            return dp[(n,cap)]
        
        dp[(n,cap)] = helper(n-1, cap)
        return dp[(n,cap)]
    
    return helper(N, W)

print(knapsack_unbounded(3,2,[1,1], [2,1]))



def knapsack(N, W, wt, val):
    dp = [[0]*(W + 1) for _ in range(N)]

    for i in range(N):
        for j in range(W+1):
            
            cv = val[i] 
            cw = wt[i]

            if i == 0:
                dp[i][j] = (j//cw)*cv

            cv = val[i] 
            cw = wt[i]

            if cw <= j: 
                dp[i][j] = max(cv + dp[i][j-cw], dp[i - 1][j])
            else:
                dp[i][j] = dp[i-1][j]

    return dp[N-1][W]

print(knapsack(2,3,[2,1],[1,1]))

# ------------------------------------------using 1D array -----------------------------------------

def knapsack(N, W, wt, val):
    dp = [0]*(W + 1)

    for i in range(N):
        for j in range(W+1):
            
            cv = val[i] 
            cw = wt[i]

            if i == 0:
                dp[j] = (j//cw)*cv

            cv = val[i] 
            cw = wt[i]

            if cw <= j: 
                dp[j] = max(cv + dp[j-cw], dp[j])
            else:
                dp[j] = dp[j]

    return dp[W]

print(knapsack(2,3,[2,1],[1,1]))