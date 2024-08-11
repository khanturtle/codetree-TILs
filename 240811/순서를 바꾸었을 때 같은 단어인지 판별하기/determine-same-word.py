arr = input()
arr2 = input()
arr = list(arr)
arr2 = list(arr2)
arr.sort()
arr2.sort()

def arr_compare(arr,arr2):
    if(len(arr)!=len(arr2)):
        return False
    for i in range(len(arr)):
        if(arr[i]!=arr2[i]):
            return False
    return True

if(arr_compare(arr,arr2)):
    print("Yes")
else:
    print("No")