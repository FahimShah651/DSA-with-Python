def insertion_sort_recursive(arr, n):
    print(f"inside the recursion : {arr} ")
    if n <= 1:
        return
    insertion_sort_recursive(arr, n-1)

    last = arr[n-1]
    j = n-2

    while j >= 0 and arr[j] > last:
        print(f"inside the while : {arr} ")
        arr[j+1] = arr[j]
        j -= 1

    arr[j+1] = last

arr = [5, 2, 7, 1, 3]
n = len(arr)

insertion_sort_recursive(arr, n)

print("Sorted array:", arr)
