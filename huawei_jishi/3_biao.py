#!/usr/env/python3

while True:
    try:
        m,n=list(map(int,input().split()))
        exchange=list(map(int,input().split()))
        insertrow=int(input())
        insertcol=int(input())
        trace=list(map(int,input().split()))
        res=[]
        if 0<=m<=9 and 0<=n<=9:
            res.append(0)
        else:
            res.append(-1)

        if 0<=exchange[0]<=m-1 and 0<=exchange[1]<=n-1 and 0<=exchange[2]<=m-1 and 0<=exchange[3]<=n-1:
            res.append(0)
        else:
            res.append(-1)

        if 0<=insertrow<=m-1:
            res.append(0)
        else:
            res.append(-1)

        if 0<=insertcol<=n-1:
            res.append(0)
        else:
            res.append(-1)

        if 0<=trace[0]<=m-1 and 0<=trace[1]<=n-1:
            res.append(0)
        else:
            res.append(-1)

        for i in res:
            print(i)
    except:
        break
