# Contains Duplicate
def Find_twice(arr):
    n=len(arr)
    for i in range(n):
        for j in range(i+1,n):
            if arr[i]==arr[j]:
                return True
            j+=1
        return False
arr=[1,2,3,6]
ans=Find_twice(arr)
print(ans)
 