def perfect_sum(arr, n, sm):
    arr.sort(reverse=True)
    def solve(n,sm):
    
        if n == 0:
            if sm == 0:
                return 1
            else:
                return 0
        
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
        return c
    
    return solve(n, sm)

print(perfect_sum([1,2,3,4,5], 5, 10))

# ---------------------------------------------- top_down/ memoization ----------------------------------------
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

#----------------------------------------------- bottom-up----------------------------------------------

# def perfect_sum(arr, n, sm):
#     arr.sort(reverse=True)
#     def solve(n,sm):
#         dp = [[0]*(sm+1) for _ in range(n) ]
        
#         for i in range(n):
#             for j in range(sm+1):
                
#                 sm = j
#                 item = arr[i]

#                 if i == 0:
#                     if sm == 0:
#                         if item == 0:
#                             dp[i][j] = 2
#                         else: dp[i][j] = 1
#                     else:
#                         if item == sm:
#                             dp[i][j] = 1
#                 else:        
#                     if item<=sm:
#                         dp[i][j] = dp[i-1][sm-item]+dp[i-1][sm]
#                     else:
#                         dp[i][j] = dp[i-1][sm]

#             return dp[n-1][sm]
#     return solve(n, sm)

# print(perfect_sum([1,2,3,4,5], 5, 10))

