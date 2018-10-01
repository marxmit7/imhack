  

def insertionSort(alist):

    for index in range(1, len(alist)):
        position = index
        currentValue = alist[index]

        while position > 0 and alist[position - 1] > currentValue:
            alist[position] = alist[position - 1]
            position = position - 1

        alist[position] = currentValue



def main():
    alist = [5,4,3,2,1]

    insertionSort(alist)

    print("Sorted: " + str(alist) + "\n")


main()
