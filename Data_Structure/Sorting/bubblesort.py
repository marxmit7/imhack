def bubbleSort(data):
    for roundpassed in range(len(data)-1,0,-1):
        for i in range(roundpassed):
            if(data[i] > data[i+1]):
                temp = data[i]
                data[i] = data[i+1]
                data[i+1] = temp
    return data

data = [5,4,7,12,3]
print(bubbleSort(data))