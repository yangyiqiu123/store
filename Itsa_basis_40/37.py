while True:
    try:
        dict1={}

        sum=0
        for i in range(4):
            num = int(input())
            if num not in dict1.keys():
                dict1[num]=1
            else:
                dict1[num]+=1
            sum+= num

        g=0
        for i in dict1.keys():
            if dict1[i]==2:
                g=1
                if len(dict1)!=2:
                    print(sum-2*i)
                    break
                else:
                    print(max(dict1.keys())*2)
                    break
            if dict1[i]==4:
                g=1
                print("WIN")
        if g==0:
            print("R")
    except:
        break