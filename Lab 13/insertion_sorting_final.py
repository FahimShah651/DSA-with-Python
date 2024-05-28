def insertion_sort(arr):
    for i in range (1,len(arr)):
        left_move = arr[i]
        j =  i-1
        while j>=0 and left_move < arr[j]:
            arr[j+1] = arr[j]
            j = j-1
            
        arr[j+1] =left_move    
        
            
arr  = [5,9,3,1,2,8,4,7,6] 
insertion_sort(arr)
print(arr)    
        