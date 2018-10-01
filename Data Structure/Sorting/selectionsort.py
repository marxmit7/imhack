def selectionSort(data):
    min_index = 0
    for i in range(data_length):
        min_index = i
        j = i+1
        for j in range(i+1,data_length):
            if (data[j] < data[min_index]):
                min_index = j
        data[i],data[min_index] = data[min_index],data[i]
    return data

data = [7,8,1,2,65,32,20,41,21,0]
data_length = len(data)
print(selectionSort(data))