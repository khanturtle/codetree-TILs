def print_stars(n):
    print("*" * n)

def print_asc(n):
    for i in range(1,n+1):
        print_stars(i)

n = int(input())
print_asc(n)