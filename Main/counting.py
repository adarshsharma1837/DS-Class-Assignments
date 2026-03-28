def operation_counting(arr):
    count = 0
    for i in arr: 
        count += 1
    return count

arr = [1,2,3,4,5]
print("Operations:", operation_counting(arr))