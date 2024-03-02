import sys
input = sys.stdin.readline

tc = int(input())
for i in range(tc):
    n =int(input())
    dp = [ [0]*(n+1) for _ in range(2)]
    #print(dp)
    x1= list(map(int,input().split()))
    x2 = list(map(int, input().split()))
    arr_x = [x1,x2]

    for j in range(1,n+1):
        dp[0][j] = max(dp[1][j-1]+arr_x[0][j-1], dp[0][j-1])
        dp[1][j] = max(dp[0][j-1]+arr_x[1][j-1], dp[1][j-1])

    print(max(dp[0][n],dp[1][n]))