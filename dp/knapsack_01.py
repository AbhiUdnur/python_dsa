# ----------------------------------------- recursion-----------------------------------------------

def knapsack_01(W, wt, val, N):
    def helper(n, cap):
        if n==0 or cap == 0:
            return 0
        
        cwt = wt[n-1]
        cv = val[n-1]

        if cwt <= cap:
            c1 = cv+helper(n-1, cap-cwt)
            c2 = helper(n-1, cap)
            return max(c1, c2)
    
        return helper(n-1, cap)
    
    return helper(N, W)

# print(knapsack_01(50, [15,30,45], [60, 100,150],3))

# ----------------------------------------- recursion (top_down/ memoisation)-----------------------------------------------

def knapsack_01(W, wt, val, N):
    dp = {}
    def helper(n, cap):
        if n==0 or cap == 0:
            return 0
        if (n, cap) in dp:
            return [(n,cap)]
        
        cwt = wt[n-1]
        cv = val[n-1]

        if cwt <= cap:
            c1 = cv+helper(n-1, cap-cwt)
            c2 = helper(n-1, cap)
            c = max(c1, c2)
        else:
            c = helper(n-1, cap)
        
        dp[(n,cap)] = c
        return c

    return helper(N, W)

# print(knapsack_01(50, [15,30,45], [60, 100,150],3))

# -----------------------------------------iterative (bottom_up/ tabulation)-----------------------------------------------


def knapsack_01(W, wt, val, N):
    dp = [[0]*(W+1) for _ in range(N) ]

    for i in range(N):
        for j in range(W+1):
            cap = j
            cwt = wt[i] 
            cv = val[i]

            if i == 0:
                if cwt<= cap:
                    dp[i][j] = cv
                else:
                    dp[i][j] = 0
            else:
                if cwt<=cap:
                    c1 = cv+dp[i-1][cap-cwt]
                    c2 = dp[i-1][cap]
                    dp[i][j] = max(c1,c2)
                else:
                    dp[i-1][j] = dp[i-1][cap]
    
    return dp[N-1][W]
print(knapsack_01(4, [4,5,1], [1,2,3],3))
print(knapsack_01(50, [15,30,45], [60, 100,150],3))