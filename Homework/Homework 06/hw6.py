# Made by Gordon Lau


# is odd lambda function
is_odd = lambda x: x % 2 != 0

is_odd(3) 


#  Advanced lambda Function
#     - Create a lambda function that takes a list and returns their sum

# thought iterarating through items in the list and adding them together
# howerver, i found this solution while reading the documentation examples


# can be used to skim through each item in the list
# x = lambda x: list(map(print, x))

sum_list = lambda x: sum(x)

sum_list([1, 2, 3, 4, 5])



# - Sorting with Lambda

# taken inspiration from the previous example, to not make things so complicated and just used given function funcs
sort_list = lambda x: sorted(x)
print(sort_list([1, 5, 3, 8, 2]))



# - Filtering with Lambda - `filter()` 

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# filter(lambda x: x % 2 != 0, list1)

# filter allows all the odd values to pass

print(list(filter(lambda x: x % 2 != 0, list1)))


# Mapping with Lambda - `map()`

mapmap = lambda x: list(map(lambda x: x * 2, x))

print(mapmap([1, 2, 3, 4, 5]))





# - Reducing with Lambda -  `reduce()` 

from functools import reduce

nums = [1, 2, 3, 4, 5]
pn = reduce((lambda x, y: x * y), nums) # Initializer is 1 for product
print(pn)




# Enumerate with or without Lambda - `enumerate()`

enum = lambda x: list(enumerate(x))

arr = ["a", "b", "c", "d", "e"]
print(enum(arr))



# - zip with or without lambda (may combine enumerate like in class) - `zip()

yes = lambda x, y: list(zip(x, y))

print(yes([1,2,3,4,5],["a",'b',"c",'d',"e"]))
