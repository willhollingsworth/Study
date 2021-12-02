#https://www.codewars.com/kata/5279f6fe5ab7f447890006a7/train/python
from codewars_test import test_framework as Test

def pick_peaks(arr):
    dic = {"pos":[],'peaks':[]}
    for x in range(1,len(arr)-1):   # ensure the loop doesnt contain the first or last
        cur = arr[x]
        if cur > arr[x-1]:
            if cur > arr[x+1]:
                dic['pos'].append(x)
                dic['peaks'].append(cur)
            elif cur == arr[x+1]:
                for y in range(x+1,len(arr)):
                    if cur < arr[y]:
                        break
                    elif cur > arr[y]:
                        dic['pos'].append(x)
                        dic['peaks'].append(cur)
                        break
    return dic
# Test.assert_equals(pick_peaks([2,3,5,5,4,3]), {"pos":[2], "peaks":[5]})
# Test.assert_equals(pick_peaks([1,2,2,1]), {"pos":[1], "peaks":[2]})
# Test.assert_equals(pick_peaks([1,2,5,4,3,2,3,6,4,1,2,3,3,4,5,3,2,1,2,3,5,5,4,3]), {"pos":[2,7,14,20], "peaks":[5,6,5,5]})

# {'pos': [2, 7, 14, 20, 20], 'peaks': [5, 6, 5, 5, 5]}
# {'pos': [2, 7, 14, 20], 'peaks': [5, 6, 5, 5]}

Test.assert_equals(pick_peaks([1,2,3,6,4,1,2,3,2,1]), {"pos":[3,7], "peaks":[6,3]})
Test.assert_equals(pick_peaks([3,2,3,6,4,1,2,3,2,1,2,3]), {"pos":[3,7], "peaks":[6,3]})
Test.assert_equals(pick_peaks([3,2,3,6,4,1,2,3,2,1,2,2,2,1]), {"pos":[3,7,10], "peaks":[6,3,2]})
Test.assert_equals(pick_peaks([2,1,3,1,2,2,2,2,1]), {"pos":[2,4], "peaks":[3,2]})
Test.assert_equals(pick_peaks([2,1,3,1,2,2,2,2]), {"pos":[2], "peaks":[3]})
Test.assert_equals(pick_peaks([2,1,3,2,2,2,2,5,6]), {"pos":[2], "peaks":[3]})
Test.assert_equals(pick_peaks([2,1,3,2,2,2,2,1]), {"pos":[2], "peaks":[3]})
Test.assert_equals(pick_peaks([1,2,5,4,3,2,3,6,4,1,2,3,3,4,5,3,2,1,2,3,5,5,4,3]), {"pos":[2,7,14,20], "peaks":[5,6,5,5]})
Test.assert_equals(pick_peaks([]),{"pos":[],"peaks":[]})
Test.assert_equals(pick_peaks([1,1,1,1]),{"pos":[],"peaks":[]})