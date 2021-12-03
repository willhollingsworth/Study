def plusMinus(arr):
    size = len(arr)
    results = [0,0,0]
    for x in arr:
        if x>0:
            results[0] += 1
        elif x<0:
            results[1] += 1
        else:
            results[2] += 1
    # print(results)
    for y in range(3):
        results[y] = round(results[y]/size,6)
        print(results[y])
    return
    # print(results)
    # return results
    
    
    
print(plusMinus([-4, 3, -9, 0, 4, 1]))