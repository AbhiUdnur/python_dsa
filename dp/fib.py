# ------------------------------------------------ Recursive(memoisation/top_down) Method --------------------------------------------------#
def fib(n, dp):
    if n == 0:
        return 0

    if n == 1:
        return 1

    if dp[n]!=-1:
        return dp[n]

    else:
        dp[n] = fib(n-1, dp)+ fib(n-2, dp)
        return dp[n]

n = 5
print(fib(n, dp=[-1]*(n+1)))

# ------------------------------------------------ Iterative(tabulation/bottom_up) Method --------------------------------------------------#
def fib(n):
    dp = [0]*(n+1)
    dp[0]=0
    dp[1]=1
    for i in range(2,n+1):
        dp[i] = dp[i-1]+dp[i-2]
    return dp[n]

print(fib(5))


        