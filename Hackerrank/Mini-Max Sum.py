def miniMaxSum(arr):
    low,high = sum(arr), 0
    for x in range(5):
        r = sum(arr)-arr[x]
        if low > r : low = r
        if high < r : high = r
    print(low,high)    
    return
    
    
    
a1 = [1,3,5,7,9]
miniMaxSum(a1)