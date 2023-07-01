
dict={}
str=input() 
str=str.lower()
# y=str
# for u in y:
#     if not u.isalpha():
#         y=y.replace(u,' ')
    
# y=str
for u in str:
    if not u.isalpha():
        str=str.replace(u,' ')    
# print(str)
# if len(str)<=100 :
#     if str[0]!=' ' or str[1]!=' ':
long=len(list(str.split()))
print(long)

for i in str:
    # if i.isalpha():
    if i!=' ':
        if i not in dict.keys():
            dict[i]=1
        else:
            dict[i]+=1
# print(dict)
# for a,b in sorted(dict.items(),key=lambda x:(-x[1],ord(x[0]))):
#     print(f"{a} : {b}")
for a in sorted(dict.keys(),key=lambda x:ord(x)):
    print(f"{a} : {dict[a]}")