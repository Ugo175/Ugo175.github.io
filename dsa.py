def selection_sort(array):
    for i in range(len(array)):
        min_index = i
        
        for j in range(i+1, len(array)):
            if array[j] < array[min_index]:
                min_index = j

        array[i], array[min_index] = array[min_index], array[i]

    print(array)
            
                
selection_sort([5,4,3,7,6])

def merge_sort(array):
    if len(array) > 1:
        mid = len(array)//2
        leftside = array[:mid]
        rightside = array[mid:]
        
        i,j,k = 0,0,0
        
        while i< len(leftside) and j< len(rightside):
            if leftside[i] < rightside[j]:
                array[k]=leftside[i]
                i+=1
            else:
                array[k]= rightside[j]
                j+=1
            k+=1
            
        while i< len(leftside):
                array[k]=leftside[i]
                i+=1
                k+=1
        while j< len(rightside):
                array[k]=rightside[j]
                j+=1
                k+=1  
    return array

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        
        merge_sort(left_half)
        merge_sort(right_half)

        i, j, k = 0, 0, 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
            
    return arr

# Example usage:
print(merge_sort([64, 25, 12, 22, 11]))






















