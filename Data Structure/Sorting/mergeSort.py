import random
def mergeSort(alist):
    if len(alist)>1:
        mid = len(alist)/2
        lefthalf = alist[:int(mid)]
        righthalf = alist[int(mid):]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0

        while i <len(lefthalf) and j<len(righthalf):
            if lefthalf[i] <righthalf[j]:
                alist[k]= lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k = k+1
        while i<len(lefthalf):
            alist[k]=lefthalf[i]
            i = i+1
            k= k+1
        while j<len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1


alist= random.sample(range(300), 10)    #picking 10 numbers randomly that lies in the range of [0,300)
print("The List before sorting-",alist)
mergeSort(alist)
print("The List after sorting-",alist)
