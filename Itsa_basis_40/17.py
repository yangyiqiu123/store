str=input().lower()
str=list(str.split())
ans=[]
for i in str:
    if i not in ans:
        ans.append(i)
print(*ans,sep=' ')