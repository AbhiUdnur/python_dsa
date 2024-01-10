def min_sum_partition(arr,n):
    sm = sum(arr)

    def solve(n, p1,sm):
        p2 = sm-p1
        if n==0:
            return p1-p2
        
        value = arr[n-1]

        if p1-value >= p2+value:

            return min(solve(n-1, p1-value, sm), solve(n-1,p1,sm))
        
        return solve(n-1,p1,sm)
    
    return solve(n, sm,sm)
print(min_sum_partition([1,6,11,5], 4))

# ---------------------------------------------------------------- top-down/ memoisation ----------------------------------------------------

def min_sum_partition(arr,n):
    
    sm = sum(arr)
    dp = {}

    def solve(n, p1,sm):
        
        p2 = sm-p1
        if n==0:
            return p1-p2
        
        if (n,p1) in dp:
            return dp[(n,p1)]

        value = arr[n-1]
    
        if p1-value >= p2+value:
            c =  min(solve(n-1, p1-value, sm), solve(n-1,p1,sm))
        else:
            c  = solve(n-1,p1,sm)
    
        dp[(n,p1)] = c
        return c
    
    return solve(n, sm,sm)
print(min_sum_partition([1,6,11,5], 4))

