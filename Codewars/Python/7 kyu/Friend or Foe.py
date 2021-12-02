'''
Make a program that filters a list of strings and returns a list with only your friends name in it.

If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, you can be sure he's not...

Ex: Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]

i.e.

friend ["Ryan", "Kieran", "Mark"] `shouldBe` ["Ryan", "Mark"]
Note: keep the original order of the names in the output.
Test.assert_equals(friend(["Ryan", "Kieran", "Mark",]), ["Ryan", "Mark"])
'''

testval = ["Ryan", "Kieran", "Jason", "Yous"]

def friend(in_list):
    out_list = []
    for x in in_list:
        if len(x) == 4:
            out_list.append(x)
    return out_list

def beter_friend(in_list):
    #after reading the best solution, use list comprehension
    #short https://medium.com/better-programming/list-comprehension-in-python-8895a785550b
    #longer https://realpython.com/list-comprehension-python/
    
    return[x for x in in_list if len(x) == 4]


print(friend(testval))
print(friend(["Ryan", "Kieran", "Jason", "Yous"]))
print(friend(["1234", "12345", "2345", "4567"]))

print(beter_friend(testval))
print(beter_friend(["Ryan", "Kieran", "Jason", "Yous"]))
print(beter_friend(["1234", "12345", "2345", "4567"]))
