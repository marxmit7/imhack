import os

def partition(arr,low,high):
    i = low-1
    pivot =arr[high]
    for j in range(low,high):
        if arr[j] <=pivot:
            i=i+1

            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[high] = arr[high] , arr[i+1]
    return ( i+1 )

def quickSort(arr,low,high):
    if low < high:
        pi = partition(arr,low,high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)


# # test the test cases'
# filepath = os.path.dirname()
# with open(filepath+"qSortTestCase1.txt","r") as data:
#     print(data)
arr = [6, 53, 61, 79 ,88 ,104 ,110, 115,119,123,130,132,145,151,155,159,176,180,191,194]
n = len(arr)
quickSort(arr,0,n-1)
print ("Sorted array:",arr)