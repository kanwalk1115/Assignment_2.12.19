def smallest_no(arr,n):
    min = arr[0]
    for i in range(1,n):
        if arr[i] < min:
            min = arr[i]
    return min

arr =[ -1, 2, 3, 4, 5, -8, 6, 7, 8, 9]
n= len(arr)
ans = smallest_no(arr,n)
print(f"Smallest in this array is", {ans})
