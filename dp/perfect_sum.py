def perfect_sum(arr, n, sm):
    arr.sort(reverse=True)
    def solve(n,sm):
        dp = {}
        if n == 0:
            if sm == 0:
                return 1
            else:
                return 0
        if (n,sm) in dp:
            return dp[(n,sm)]
        item = arr[n-1]
        if item<=sm:
            c1 = solve(n-1, sm-item)
            c2 = solve(n-1, sm)
            c = c1+c2
        else:
            if sm==0:
                c=1
            else:
                c=0
        
        dp[(n,sm)]=c
        return c
    
    return solve(n, sm)

print(perfect_sum([1,2,3,4,5], 5, 10))