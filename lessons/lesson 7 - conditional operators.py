# we use these operators to compair different variable to each other
# when using operators, the return value is a boolean
# operator is eather True or False

# ==    checks if 2 vars are equal
# !=    checks if 2 vars are not equal
# <=    checks if a var is smaller or equal to another
# >=    checks if a var is greater or equal to another
# <     checks if a var is smaller than another
# >     checks if a var is greater than another

print("hello" == "hello")
print(1 > 1.2)
print(2.6 <= 2.6)
print("hello" != "world")
print("a" > "Z") #according to the ascii table
#print("what" > 0) throws an error

# chained conditions
x = 3
y = 7
greeting = "hello"
print(1 < 5 < 7)
print(y < x+4) # this is gonna compare 7<7 which returns False since 7=7

# special keywords for combining conditions
# and   both conditions have to be True
# or    one or both condition can be True
# not   returns the opposite boolean
# is    checks if both objects share the same identity
print(1 < 0 or greeting == "hello")
print(1 < 0 and greeting == "hello")
print(not (1 < 0)) 
print(not (True or False)) # remember BEDMAS

# (is not) vs (!=)
""" from stack overflow
== is an equality test. It checks whether the right hand side and the left hand side
are equal objects (according to their __eq__ or __cmp__ methods.)

is is an identity test. It checks whether the right hand side and the left hand side
are the very same object. No methodcalls are done, objects can't influence the is operation.
"""

# essentially (is not) is different than (!=)
# throught the project we're gonna build, we'll mostly be using (!=)
