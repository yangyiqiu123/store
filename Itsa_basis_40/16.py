a=input()
b=input()
ans=0
for i in range(len(b)):
    if b[i:i+len(a)]==a:
        ans+=1
print(ans)