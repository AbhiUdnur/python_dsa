# -------------------------------------------------------recursion--------------------------------------------
def subset_sum(N, arr,sum):
    def solve(n, sm):
        if sm ==0:
            return 1

        if n == 0:
            return 0

        item = arr[n-1]
        if item<= sm:
            c1 = solve(n-1,sm-item)
            c2 = solve(n-1,sm)

            return c1 or c2
    
        return solve(n-1,sm)

    return solve(N, sum)

# print(subset_sum(6,[3,34,4,12,5,2],9))

# ------------------------------------------------ top_down/memoization---------------------------------------
def subset_sum(N, arr,sum):
    def solve(n, sm):
        dp = {}
        arr.sort(reverse=True)
        if sm ==0:
            return 1

        if n == 0:
            return 0
        if (n,sm) in dp:
            return dp[(n,sm)] 
        
        item = arr[n-1]
        if item<= sm:
            c1 = solve(n-1,sm-item)
            c2 = solve(n-1,sm)
            c=c1 or c2
        else:
            c=0

        dp[(n,sm)] =c
        return c

    return solve(N, sum)

# print(subset_sum(6,[3,34,4,12,5,2],9))

# ------------------------------------------------- bottom-up/tabulation -------------------------------------

def subset_sum(N, arr, sum):
    def solve(n, sm):
        dp = [[0]*(sum+1) for i in range(N)]

        for i in range(N):
            for j in range(sum+1):
                item = arr[i]
                sm = j
                if i==0:
                    if item==sm or sm==0:
                        dp[i][j] = 1
                else:
                    if item <= sm:
                        dp[i][j] = dp[i-1][sm-item] or dp[i-1][sm]
                    else:
                        dp[i][j] = dp[i-1][sm]
        print(dp)
        return dp[N-1][sm]
    
    return solve(N,sum)

print(subset_sum(6,[3,34,4,12,5,2],9))






