while True:
    try:
        
        for _ in range(int(input())):
            
            a, b = input().split()
            a=a[::-1]
            b=b[::-1]
           
            length = max(len(a), len(b))
            add = 0
            ans=""
            
            for i in range(length):
                
                num=add
                
                if i < len(b):
                    num+=int(b[i])
                if i <len(a):
                    num+=int(a[i])
                
                if num//10>0:
                    add = 1
                    ans+=str(num%10)
                else:
                    ans+=str(num%10)
                    add = 0
            
            if add!=0:
                ans+=str(add)
            print(ans[::-1])
    except:
        break

# while True:
#   try:
#     n = int(input())
#     for i in range(n):
#       n1,n2 = map(int,input().split()) 
#       print(n1+n2)
#   except:
#     break