# there are 2 main types of loops in python 
# for loops 
# and while loops 

# for loops allow us to iterate (loop) for a set numebr of times
# while loops allow us to iterate as long a condition is true

# print numbers 0 to 10 (excluding 10)
for i in range(10): # range is a special function in python that creates a collection of nubers
    print(i)        # depending on its arguements
print("\n") # new line character

# these are the args of range but the default for start is 0 and step is 1
# range(start, stop, step)
for i in range(4, 20, 2):
    print(i)

# for loops can print elements in collections like lists
for i in ["hello", "world", "of", "python"]:
    print(i)

# you can also get the index of each element with the element itself while looping through a list
print("\n")
lst = ["wow", "that", "was", "really", "cool"]
for index, elem in enumerate(lst):
    print(f"element '{elem}' is at index {index}")

# to exit a for loop before it has finish looping over the givin # of times use break ketword
print("\n")
lst = ["wow", "that", "was", "really", "cool"]
for index, elem in enumerate(lst):
    if index == 3:
        break
    print(f"element '{elem}' is at index {index}")

# excersise 5
# program a "guess the numeber" game which which allowes the user 3 tries
# to guess a number between 1 and 10. If their guess is less or greater
# than the secrete numebr then tell the player.
