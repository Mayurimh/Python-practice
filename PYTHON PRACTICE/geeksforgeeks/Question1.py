# Maximum and minimum of an array using minimum number of comparisons

# solution 1
# def MaxNumber(arr1):
#     max=float('-inf')
#     for num in arr1:
#         if num>max:
#           max=num
#     return max

# def MinNumber(arr1):
#     min=float('inf')
#     for num in arr1:
#         if num<min:
#           min=num
#     return min

# if __name__=="__main__":
#     arr1=[22, 14, 8, 17, 35, 3]
#     print("Maximum number is : ",MaxNumber(arr1))
#     print("Minimum Number is : ",MinNumber(arr1))
    
# solution 2

def MaxMin(arr):
    arr.sort()
    minmax={'min':arr[0],'max':arr[-1]}
    return minmax
arr=[34,54,2,33,0,84]
minmax=MaxMin(arr)
print("max number is : ",minmax["max"])
print("min number is : ",minmax["min"])