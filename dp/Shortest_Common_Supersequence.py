def s_Cs(s1,s2,m,n):

    dp = [[0]*(n+1) for i in range(m+1)]

    for i in range(1,m+1):
        for j in range(1,n+1):

            if s1[i-1] == s2[j-1]:
                dp[i][j] = 1+dp[i-1][j-1]
            
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    lcs = dp[m][n]
    return (m+n)-lcs

print(s_Cs('ABC', "AC",3,2))

