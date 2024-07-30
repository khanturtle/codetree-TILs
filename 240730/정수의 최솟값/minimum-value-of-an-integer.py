def answer(a,b,c):
    if(a<b):
        if(a<c):
            return a
        else:
            return c
    else:
        if(b<c):
            return b
        else:
            return c

a,b,c = tuple(map(int,input().split()))
print(answer(a,b,c))