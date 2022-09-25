name = input("name") # question: what will be the value of name?

if name == "adam":
    print("we are inside the if statement now") # if the first if statment condition was false
elif name == "noah":                            # we will check the elif conditions
    print("we are inside the first elif statement now")# but if the if statement was true then we
elif name == "cogswell":                        # will skip the elif statements
    print("we are inside the second elif statement now") # we can have as many elif statements
else:
    print("we are inside the else statement")   # if the if statement and all the elif statements 
                                                # were falls, we will execute the code inside the else statement
# indentation is important!!!
print("Always do this") # anything outside the if structure will run no matter 
                        # the conditions of the if statements

# excersise 3
# write a program that will take the age of a person and print out if they are over 18 or not
