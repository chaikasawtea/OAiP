def find_max(arr):
    if len(arr) == 1:
        return arr[0]
    
    mid = len(arr) // 2
    left = find_max(arr[:mid])
    right = find_max(arr[mid:])
    
    if left > right:
        return left
    else:
        return right
    
numbers = [3,7,1,9,4,2]
print(find_max(numbers))