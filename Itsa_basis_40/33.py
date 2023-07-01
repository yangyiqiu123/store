while True:
    try:
        num=list(map(int,input().split()))
        print(f"Size: {len(num)}")
        s=sum(x for x in num)
        rounded_num = round(s/len(num),3)
        print(f"Average: {rounded_num:.3f}")
    except:
        break