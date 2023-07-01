game=[]
win = 0
for _ in range(3):
    game.append(list(map(int,input().split())))

# 橫
for i in range(3):
    if game[i]==[0,0,0] or game[i]==[1,1,1]:
        win = 1
        break

for i in range(3):
    if [game[0][i],game[1][i],game[2][i]]==[0,0,0] or [game[0][i],game[1][i],game[2][i]]==[1,1,1]:
        win = 1
        break
        
if [game[0][0],game[1][1],game[2][2]]==[0,0,0] or [game[0][0],game[1][1],game[2][2]]==[1,1,1]:
    win = 1
    
if [game[0][2],game[1][1],game[2][0]]==[0,0,0] or [game[0][2],game[1][1],game[2][0]]==[1,1,1]:
    win = 1
    
if win == 1:
    print("True")
else:
    print("False")