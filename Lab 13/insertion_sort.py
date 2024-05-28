def insertion_sort(arr, sorted = list()):
    len_arr =len(arr)
    if len_arr == 0 :
        arr = sorted
        print(f"before return : {arr}")
        return arr
    
    sorted.append(arr[0])
    print(sorted)
    
    for i in sorted:
        print(f"index is : {i}")
        if arr[1] < i:
            sorted.insert(0,arr[1])
        else:
            sorted.append(arr[1])
    
    insertion_sort(arr[:(len_arr-1)],sorted)

arr  = [5,3,4,7,2,8,6,9,1]  
sorting = list()
insertion_sort(arr,sorting)

print(arr)
print(sorting)

    