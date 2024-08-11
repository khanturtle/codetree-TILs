arr = input()
arr2 = input()
arr = list(arr)
arr2 = list(arr2)
arr.sort()
arr2.sort()

def arr_compare(arr,arr2):
    arrlen=0
    if(len(arr)>=len(arr2)):
        arrlen=len(arr)
    else:
        arrlen=len(arr2)

    for i in range(arrlen):
        if(arr[i]!=arr2[i]):
            return False
    return True

if(arr_compare(arr,arr2)):
    print("Yes")
else:
    print("No")