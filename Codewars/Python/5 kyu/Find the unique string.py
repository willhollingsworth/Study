
''' simple approach'''
# def find_uniq(arr):
#     for i,a in enumerate(arr):
#         current = filter(a)
#         next = arr[(i+1) % len(arr)]
#         two_forward = arr[(i+2) % len(arr)]
#         if current != filter(next):
#             if current != filter(two_forward):
#                 return a
#             else:
#                 return next

# def filter(string):
#     return set([c.lower() for c in string.strip()])

''' too slow but does work'''
# from collections import Counter
# def find_uniq(arr):
#     filtered_list = [set(a.lower()) for a in arr]
#     for i,val in enumerate(filtered_list):
#         if filtered_list.count(val) == 1:
#             return arr[i]
        
''' processes quick enough to pass'''
from collections import Counter
def find_uniq(arr):
    filtered_list = [''.join(set(a.lower())) for a in arr]
    uniques = set().union(filtered_list)
    count = {filtered_list.count(u):u for u in uniques}
    return arr[filtered_list.index(count[1])]

print(find_uniq([ 'Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a' ]), 'BbBb')
print(find_uniq(['BbBb', 'Aaaa', 'AaAaAa', 'a' ]), 'BbBb')
print(find_uniq([ 'abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba' ]), 'foo')
print(find_uniq([ '    ', 'a', '  ' ]), 'a')
print(find_uniq([ 'aa', 'a', 'b' ]), 'b')
# # # 