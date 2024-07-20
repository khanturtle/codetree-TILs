def gcd(a,b):
    while(b!=0):
        r=a%b
        (a,b) = (b,r)
    return abs(a)


def lcd(a,b):
    return int(a*b/(gcd(a,b)))

a,b=map(int,input().split())
print(lcd(a,b))