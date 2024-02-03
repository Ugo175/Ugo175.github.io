def selection_sort(array):
    for i in range(len(array)):
        min_index = i
        
        for j in range(i+1, len(array)):
            if array[j] < array[min_index]:
                min_index = j

        array[i], array[min_index] = array[min_index], array[i]

    print(array)
            
                
selection_sort([5,4,3,7,6])



