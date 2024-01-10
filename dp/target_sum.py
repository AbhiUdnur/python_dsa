def target_sum(arr,n, target):
    
    sm = sum(arr)
    x = sm+target
    
    if x%2 !=0:
        return
    
    x = x//2
    def solve(n,sm):

        if sm==0:
            return 1
        
        if n == 0:
            return 0
        
        item = arr[n-1]

        if item <= sm:

            return int(solve(n-1, sm-item))+int(solve(n-1, sm))
        
        return solve(n-1, sm)
    
    return solve(n, x)


print(target_sum([1,1,1,1,1],5,3))
# ---------------------------------------------------------------- top-down/ memoisation ----------------------------------------------------
def target_sum(arr,n, target):
    
    sm = sum(arr)
    x = sm+target
    dp = {}
    
    if x%2 !=0:
        return
    
    x = x//2
    
    def solve(n,sm):
        if sm==0:
            return 1
    
        if n == 0:
            return 0
    
        if (n,sm) in dp:
            return dp[(n,sm)]
    
        item = arr[n-1]
    
        if item <= sm:
            dp[(n,sm)] = solve(n-1, sm-item)+ solve(n-1, sm)
            return dp[(n,sm)]
    
        dp[(n,sm)] = solve(n-1, sm)
        return dp[(n,sm)]
    
    return solve(n, x)

print(target_sum([1,2,3,1],4,3))