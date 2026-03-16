class Connect4:
    def __init__(s): s.board=[[0]*7 for _ in range(6)];s.turn=1
    def display(s):
        syms={0:".",1:"X",-1:"O"}
        for row in s.board: print(" ".join(syms[c] for c in row))
        print(" ".join(str(i) for i in range(7)))
    def drop(s,col):
        for r in range(5,-1,-1):
            if s.board[r][col]==0: s.board[r][col]=s.turn;s.turn*=-1;return r
        return -1
    def undo(s,col):
        for r in range(6):
            if s.board[r][col]!=0: s.board[r][col]=0;s.turn*=-1;return
    def check_win(s):
        for r in range(6):
            for c in range(7):
                if s.board[r][c]==0: continue
                p=s.board[r][c]
                for dr,dc in[(0,1),(1,0),(1,1),(1,-1)]:
                    if all(0<=r+dr*i<6 and 0<=c+dc*i<7 and s.board[r+dr*i][c+dc*i]==p for i in range(4)):
                        return p
        return 0
    def valid_moves(s): return [c for c in range(7) if s.board[0][c]==0]
    def minimax(s,depth,maximizing):
        w=s.check_win()
        if w: return w*100
        if depth==0 or not s.valid_moves(): return 0
        if maximizing:
            best=-999
            for c in s.valid_moves():
                s.drop(c);val=s.minimax(depth-1,False);s.undo(c)
                best=max(best,val)
            return best
        else:
            best=999
            for c in s.valid_moves():
                s.drop(c);val=s.minimax(depth-1,True);s.undo(c)
                best=min(best,val)
            return best
    def best_move(s,depth=4):
        best_col=s.valid_moves()[0];best_val=-999
        for c in s.valid_moves():
            s.drop(c);val=s.minimax(depth-1,False);s.undo(c)
            if val>best_val: best_val=val;best_col=c
        return best_col
def demo():
    g=Connect4()
    for col in[3,3,4,4,5,2,5]: g.drop(col)
    g.display()
    mv=g.best_move(4);print(f"AI suggests column: {mv}")
    w=g.check_win();print(f"Winner: {'X' if w==1 else 'O' if w==-1 else 'None'}")
if __name__=="__main__": demo()
