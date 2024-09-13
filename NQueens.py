'''
[Yesterday 5:23 PM] Mohan Prasath N
The n-queens puzzle is the problem of placing n queens on an n x n 
chessboard such that no two queens attack each other.
 
Given an integer n, return all distinct solutions to the n-queens puzzle. 
You may return the answer in any order.
 
Each solution contains a distinct board configuration of the n-queens' placement, 
where 'Q' and '.' both indicate a queen and an empty space, respectively.
 
Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]'''

def NQueens(n):
    col=set()
    posDg=set() #r+c
    negDg=set() #r-c
    res=[]
    board=[["."]*n for i in range(n)]
    def solve(r):
        if r==n:
            res.append(["".join(i) for i in board])
            return
        
        for c in range(n):
            print("c=",c)
            if c in col or (r+c) in posDg or (r-c) in negDg:
                continue
            
            col.add(c)
            posDg.add(r+c)
            negDg.add(r-c)
            
            board[r][c]="Q"
            solve(r+1)
            
            col.remove(c)
            posDg.remove(r+c)  
            negDg.remove(r-c)   
            board[r][c]="."
    solve(0)
    return res

n=int(input("Enter value of n: "))
print(NQueens(n))
