def bubble_sort(arr):
    size =len(arr)
    for i in range(size-1):
        swapped = False
        for j in range(size-1-i):
            if arr[j] > arr[j+1]:
                tmp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = tmp
                swapped =True
        if not swapped:
            break



arrr = [5,9,3,1,2,8,4,7,6] 
print(f"before sorting : {arrr}")
bubble_sort(arrr)
print(f"After  sorting : {arrr}")
    