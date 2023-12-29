def equal_partition_sum(N,arr):

    if sum(arr)%2!=0:
        return 0

    sm = sum(arr)//2
    def solve(sm,n):
    
        dp = {}
        if sm==0:
            return 1
        if n==0:
            return 0
        if (sm,n) in dp:
            return dp[(sm,n)]
        
        item = arr[n-1]
        
        if item<=sm:
            c = solve(sm-item, n-1) or solve(sm, n-1)
            
        else: 
            c=0
        
        dp[(sm,n)] = c
        return c
    
    return solve(sm, N)   

print(equal_partition_sum(4,[1,5,5,11]))


    