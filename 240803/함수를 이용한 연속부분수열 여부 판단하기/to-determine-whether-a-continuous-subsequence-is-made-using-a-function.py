def in_list(a_list,b_list):
    flag = 0
    for i in range(len(a_list)-len(b_list)+1):
        for j in range(len(b_list)):
            if(a_list[i+j]==b_list[j]):
                flag = 1
            else:
                flag = 0
        if(flag):
            return True
    return False

a,b=map(int,input().split())
a_list=[]
b_list=[]

a_list = list(map(int,input().split()))
b_list = list(map(int,input().split()))

if(in_list(a_list,b_list)):
    print("Yes")
else:
    print("No")