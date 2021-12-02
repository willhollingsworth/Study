import codewars_test as test
def cakes(recipe, available):
    count = []
    for x,y in recipe.items():  
        # print(x,y,'is needed, we have ',available[x],'currently availble')

        if x in available:  # check if the recipe item is in the available list
            count.append(available[x]//y)   # if so then divide the avaible items but the recipe and discard the remainder 
        else:
            return 0
    return(min(count))




recipe = {"flour": 500, "sugar": 200, "eggs": 1}
available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
test.assert_equals(cakes(recipe, available), 2, 'example #1')

recipe = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
available = {"sugar": 500, "flour": 2000, "milk": 2000}
test.assert_equals(cakes(recipe, available), 0, 'example #2')