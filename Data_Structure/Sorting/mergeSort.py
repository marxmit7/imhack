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


alist= [165,164,158,150,144,137,135,108,103,94,92,80,65,64,52,44,10,6,6,3]
mergeSort(alist)
print(alist)