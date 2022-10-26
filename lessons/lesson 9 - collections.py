# collections are a group of data types
# there are 2 types of collections
# ordered and unordered collections

# lists are mutable ordered collections
lst1 = [1, 2, 3]
lst2 = ["hello", "world", "of", "python"]
lst3 = [True, False, False, True] 
super_list = [1, "hello", True] # lists can have several data types in them
                                # but usually, we use lists with one datatype much more than several datatypes

print(lst1) # to view the list 
print(len(lst2)) # prints the length (# of elements) of the list

# we can start with an empty list and 'append' elements to it
shopping_list = []
print(f"empty shopping list: {shopping_list}")
shopping_list.append("milk")
shopping_list.append("cookies")
shopping_list.append("candy")
shopping_list.append("bread") # append adds an element to the end of the list
print(f"filled shopping list: {shopping_list}")

# to access elements inside a list
print(shopping_list[0]) # start counting at zero

# change element at specific index
shopping_list[1] = "cake"
print(shopping_list)

# to remove an element using it's value 
shopping_list.remove("cake") # going to remove the first instance of 'cake' in the list
print(shopping_list)

# to remove element using it's index
shopping_list.pop(0) # remove elem at index 0 which is milk
# del shopping_list[0]      - this does the same thing
print(shopping_list)

# check if an element is in a list
print("cookies" in shopping_list)
print("bread" in shopping_list)

# get the index of an elem in a list
print(shopping_list.index("candy"))


# tuples are imutable ordered collections
tup1 = (1, 2, 3)
tup2 = ("hello", "world", "of", "python")
tup3 = (True, False, False, True)
super_tuple = (1, "hello", True)

print(tup1)
print(tup1[0]) # prints first element of tup1
print(len(tup1))

# tuples are immutable so the following line of code will through an error
# tup2[0] = "what!?"

# 2d lists and tuples
# i could have a list within a list or a tuple within a list 
lst_2d = [
    ['A', 'B', 'C'],
    [1, 2, 3]
]
print(lst_2d)
print(lst_2d[0])
print(lst_2d[0][1])

# excersise 4
# write a program which allows the user to check if an element
# is in a pre-defined list of strings. If it is, print out the
# element's index. If it is not, tell the the usr it isnt in the lst.
