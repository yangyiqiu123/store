for _ in range(int(input())):
    grade = list(map(int, input().split()))

    t = 0
    f = 0
    for i in range(len(grade)):
        if grade[i] >= 60:
            t += 1
        else:
            f += 1
    if t==3 or (t==2 and (sum(x for x in grade)>=220)):
        print("P")
    elif (t==2 and (sum(x for x in grade)<220)):
        print("M")
    elif f==2:
        u=0
        for i in grade:
            if i >=80:
                u=1
        if u==1:
            print("M")
        else:
            print("F")
    else:
        print("F")
        
