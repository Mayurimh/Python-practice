# Array Reverse

# solution 1
# def reverseArray(arr):
#     arr.reverse()
#     return arr

# arr=[1,2,3,4,5]
# reverseArr=reverseArray(arr)
# print("reverse array : ",reverseArr)

# solution 2
# def reverseArray_using_stack(arr):
#     stack=[]
#     for a in arr:
#         stack.append(a)
        
#     for i in range(len(stack)):
#         arr[i]=stack.pop()
    
#     print(arr)
        
# arr=[1,2,3,4,5,6,7]
# print("main array : ",arr)
# reverseArray=reverseArray_using_stack(arr)
# print("reverse array : ",reverseArray)
        
# solution 3

# def reverse_array(arr,start,end):
#     while start<end:
#         arr[start],arr[end]=arr[end],arr[start]
#         start+=1
#         end-=1
#     return arr  

# arr=[1,2,3,4,5]
# length_arr=len(arr)
# rev_arr=reverse_array(arr,0,length_arr-1)
# print("reverse array : ", rev_arr)

# solution 4

def reverse_array(arr):
    rev_arr=arr[::-1]
    print("reversed array : ",end=" ")
    for element in rev_arr:
        print(element,end=" ")

array=[1,2,3,4,5,6,7]
reverse_array(array)
    