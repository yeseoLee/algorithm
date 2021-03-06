'''
import sys
def solve(x):
    cost_sum=0
    for i in range(k-1):
        now_cost=x[0]+x[1]
        now_idx=0
        for j in range(1,len(x)-1):
            if(now_cost>x[j]+x[j+1]):
                now_cost=x[j]+x[j+1]
                now_idx=j
        
        cost_sum+=now_cost
        x[now_idx]=now_cost
        del x[now_idx+1]        
    return cost_sum       
t=int(sys.stdin.readline())
for i in range(t):
    k=int(sys.stdin.readline())
    ch=list(map(int,sys.stdin.readline().split()))
    print(solve(ch))
'''
'''
import sys
inf=100000000
def solve(s,e):
    if(e-s==1):
        dp[s][e]=sum(ch[s:e+1])
        return
    min_cost=inf
    for bd in range(s,e):
        if(s!=bd and dp[s][bd]==0):
            solve(s,bd)
        if((bd+1)!=e and dp[bd+1][e]==0):
            solve(bd+1,e)
        cost=dp[s][bd]+dp[bd+1][e]+sum(ch[s:e+1])
        if(min_cost>cost):
            min_cost=cost
    dp[s][e]=min_cost
t=int(sys.stdin.readline())
for i in range(t):
    k=int(sys.stdin.readline())
    ch=list(map(int,sys.stdin.readline().split()))
    dp=[[0 for i in range(k+1)] for j in range(k+1)]
    solve(0,k)
    print(dp[0][k-1])
'''

import sys
def sumFile(ch):
    for i in range(1,k): #길이 
        for j in range(k-i): #시작점
            mincost=99999999
            for x in range(i):
                cost=dp[j][j+x]+dp[j+x+1][j+i]
                if(cost<mincost):
                    mincost=cost
            dp[j][j+i]=mincost
            dp[j][j+i]+= (s[j+i]-s[j-1]) if j!=0 else s[j+i] #sum(ch[j:j+i+1])

t=int(sys.stdin.readline())
for i in range(t):
    k=int(sys.stdin.readline())
    ch=list(map(int,sys.stdin.readline().rstrip().split()))
    dp=[[0]*(k) for x in range(k)]
    s = [sum(ch[0:i+1]) for i in range(k)]
    sumFile(ch)
    print(dp[0][-1])

'''
import sys
input = sys.stdin.readline
T = int(input())
INF = sys.maxsize

for _ in range(T):
    K = int(input())
    file_sizes = list(map(int, input().split()))
    dp = [[0 for i in range(K)] for j in range(K)]
    S = [sum(file_sizes[0:i+1]) for i in range(K)]	
    for gap in range(1, K):
        for start in range(K - gap):
            end = start + gap
            dp[start][end] = INF
            for k in range(start, end):
                dp[start][end] = min(dp[start][end], dp[start][k] + dp[k+1][end])
            dp[start][end] += S[end] - S[start-1] if start != 0 else S[end]
    print(dp[0][-1])
'''
