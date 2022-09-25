predefined_lst = ["hello", "world", "of", "python", "adam", "noah", "cogswell"]
element = input("what element are you looking for? ")

if element in predefined_lst:
    print(f"{element} is at index {predefined_lst.index(element)}")
else:
    print(f"{element} is not in the list")
