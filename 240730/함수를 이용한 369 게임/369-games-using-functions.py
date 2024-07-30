def is_369 (a,b):
    ans=set()
    for i in range(a,b+1):
        if('3' in str(i) or '6' in str(i) or '9' in str(i)):
            ans.add(i)
    return ans

def is_3(a,b):
    ans=set()
    for i in range(a,b+1):
        if(i%3==0):
            ans.add(i)
    return ans

a,b = map(int,input().split())
ans_set = is_369(a,b) | is_3(a,b)
print(len(ans_set))