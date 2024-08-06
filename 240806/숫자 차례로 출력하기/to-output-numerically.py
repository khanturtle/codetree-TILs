def print_num(n):
    for i in range(1,n+1):
        print(i,end=' ')
    
    
def print_reverse_num(n):
    if(n==0):
        return
    print(str(n),end=' ')
    print_reverse_num(n-1)

n = int(input())

print_num(n)
print()
print_reverse_num(n)