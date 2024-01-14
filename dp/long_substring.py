def lss(s1,s2):
    a = len(s1)
    b = len(s2)
    dp = [[0]*(b+1) for i in range(a+1)]
    ans = 0
    for i in range(1,a+1):
        for j in range(1,b+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = 1+dp[i-1][j-1]
                ans = max(ans, dp[i][j])
    
    for i in range(a+1):
        for j in range(b+1):
            if dp[i][j] == ans:
                m = i
                break
    s = ''
    while ans >0 and m>0:
        s+=s1[m-1]
        m-=1
        ans-=1
    return s[::-1]

print(lss("abcd", "dabcdjipj"))
