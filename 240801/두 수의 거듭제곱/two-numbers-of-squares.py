def square(a,b):
    ans=1
    for _ in range(b):
        ans *= a

    return ans

a,b=map(int,input().split())
print(square(a,b))