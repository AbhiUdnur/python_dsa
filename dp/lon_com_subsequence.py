def lcs(x,y,s1,s2):

    if x == 0 or y == 0:
        return 0
    
    if s1[x-1] == s2[y-1]:
        return 1+lcs(x-1,y-1,s1,s2)
    
    return max(lcs(x-1,y, s1,s2), lcs(x,y-1, s1,s2))

print(lcs(3,2,'ABC', "AC"))

# ---------------------------------------------------------------------------

def lcs(x,y,s1,s2):

    dp = {}

    if x == 0 or y == 0:
        return 0
    
    if (x,y) in dp:
        return dp[(x,y)]
    
    else:
        if s1[x-1] == s2[y-1]:
            dp[(x,y)] =  1+lcs(x-1,y-1,s1,s2)

        else:
            dp[(x,y)] = max(lcs(x-1,y, s1,s2), lcs(x,y-1, s1,s2))

        return dp[(x,y)]

print(lcs(3,2,'ABC', "AC"))

# ---------------------------------------------------------------------------

def lcs(x,y,s1,s2):
    dp = [[0]*(y+1) for i in range(x+1)]

    for i in range(x+1):
        for j in range(y+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            
            else:
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
            
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
    
    ans = ""
    while x>0 and j>0:
        if s1[x-1] == s2[y-1]:
            ans+=s1[x-1]
            x-=1
            y-=1
        
        else:
            if dp[x-1][y] >= dp[x][y-1]:
                x-=1
            else:
                y-=1
                
    return ans[::-1]

print(lcs(3,2,'ABC', "AC"))