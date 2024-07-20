def gcd(a,b):
    while b != 0:
        r = a%b
        (a,b) = (b,r)
    return abs(a)



a,b=map(int,input().split())
print(gcd(b,a))