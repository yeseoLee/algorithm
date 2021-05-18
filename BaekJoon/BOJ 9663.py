'''
n=int(input())
stack=[]
result=[]
def solve(q,n):
    global result
    if(q==0):
        result.append(sorted(stack))
        return
    for i in range(n):
        for j in range(n):
            f=0
            for x,y in stack:
                if(i==x or j==y or i-j==x-y):
                    f=1
                    break
            if(f==0):
                stack.append([i,j])
                solve(q-1,n)
                stack.pop()       
solve(n,n)
unique_list=[]
for v in result:
    if v not in unique_list:
        unique_list.append(v)
print(unique_list,len(unique_list))
'''
'''
#1. 체스판 한줄에 하나의 퀸만 들어갈 수 있다.
n=int(input())
chess=[]
result=0
def solve(cnt):
    global result
    def is_possible(now_col):
        now_row=len(chess)
        for row in range(now_row):
            if(chess[row]==now_col or
               abs(chess[row]-now_col)==(now_row-row)):
                #왜 다른 식은 안될까? col-row == now_col-now_row 같은
                #대각선은 기울기 1, -1 두개니까...
                return False
        return True
    if(cnt==0):
        result+=1
        return
    for col in range(n): #들어갈 수 있는 col 찾기
        if is_possible(col):
            chess.append(col) #stack의 idx:row, value:col임
            solve(cnt-1)
            chess.pop()
            
solve(n)
print(result)
'''
n = int(input())
res = 0
board=[0]*15
def recursive(x):
    global res
    if x == n:
        res += 1
        return
    for i in range(n):
        board[x] = i
        if check(x):
            recursive(x+1)
def check(x):
    for i in range(x):
        if board[x] == board[i] or abs(board[i]-board[x]) == x-i:
            return False
    return True

recursive(0)
print(res)


