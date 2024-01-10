def rod_cut(N, price):

    def solve(cl, rl):

        if cl==0 or rl == 0:
            return 0
        
        val = price[cl-1]

        if cl<=rl:

            return max(val+solve(cl, rl-cl),solve(cl-1, rl)) 
        
        return solve(cl-1, rl)

    return solve(N, N)

print(rod_cut(8, [1,5,8,9,10,17,17,20]))


# ------------------------------------------------ top_down/memoization ------------------------------------

def rod_cut(N, price):

    def solve(cl, rl):

        dp = {}
        
        if cl==0 or rl == 0:
            return 0
        
        if (cl,rl) in dp:
            return dp[(cl,rl)]
        
        val = price[cl-1]

        if cl<=rl:

            dp[(cl,rl)] = max(val+solve(cl, rl-cl), solve(cl-1, rl))
            return dp[(cl,rl)]
        
        dp[(cl,rl)] = solve(cl-1, rl)
        return dp[(cl,rl)] 

    return solve(N, N)

print(rod_cut(8, [1,5,8,9,10,17,17,20]))

# ------------------------------------------------ bottom_up/tabulation ------------------------------------

def rod_cut(N, price):

    dp = [[0]*(N+1) for i in range(N+1)]

    for i in range(N+1):
        for j in range(N+1):
            cl=i
            rl=j

            if cl==0 or rl==0:
                dp[i][j] = 0
            
            else:
                val = price[cl-1]
                if cl<= rl:
                    c1 = val+dp[cl][rl-cl]
                    c2 = dp[cl-1][rl]
                    dp[i][j] = max(c1,c2)
                else:
                    dp[i][j] = dp[cl-1][rl]
    return dp[N][N]
        
print(rod_cut(8, [1,5,8,9,10,17,17,20]))

# ------------------------------------------------ bottom_up/tabulation ------------------------------------

def rod_cut(N, price):

    dp = [0]*(N+1)

    for rl in range(1,N+1):
        ans = 0
        for cl in range(1,rl+1):
            ans = max(ans, price[cl-1]+dp[rl-cl])
        
        dp[rl] = ans
    return dp[N]

print(rod_cut(8, [1,5,8,9,10,17,17,20]))

# ------------------------------------------------ top_down/memoization ------------------------------------

def rod_cut(N, price):
    
    dp={}
    
    def solve(rl):
        if rl==0:
            return 0
        
        if rl in dp:
            return dp[rl]

        ans = 0

        for cl in range(1,rl+1):
            ans = max(ans, price[cl-1]+solve(rl-cl))
        
        dp[rl] = ans
        return ans
    
    return solve(N)

print(rod_cut(8, [1,5,8,9,10,17,17,20]))