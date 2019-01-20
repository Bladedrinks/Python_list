# Program to insert items of "asin()", "acos()" and "atan()" to the list of trig = ["sin()", "cos()", "tan()"] in the way of
# putting each item right after its inverse, like ["sin()", "asin()", "cos()", "acos()", "tan()", "atan()"]
# Breaking the process into pieces:
# Note: list.insert(index, element) - The syntax of list.insert() method

# Step 0:
# print(trig) returns ["sin()", "cos()", "tan()"]
# index:               0        1        2

# Step 1:
# trig.insert(1, "asin()")
# print(trig) returns ["sin()", "asin()", "cos()", "tan()"]
# index:               0        1         2        3

# Step 2:
# trig.insert(3, "acos()")
# print(trig) returns ["sin()", "asin()", "cos()", "acos()", "tan()"]
# index:               0        1         2        3         4

# Step 3:
# trig.insert(5, "atan()"]
# print(trig) returns ["sin()", "asin()", "cos()", "acos()", "tan()", "atan()"]
# index:               0        1         2        3         4        5

trig = ["sin()", "cos()", "tan()"]
ls = ["asin()", "acos()", "atan()"]
#     0         1         2
i = -1   
                                                       
for item in ["asin()", "acos()", "atan()"]:           
    i += 2   # In Line 28, i (for index) is set to -1 in order to make i += 2 returns values of 1, 3, 5 once at a time.
    trig.insert(i, item)    # Why do we have to assign 1, 3, 5 to i (index indicating the position where the item is inserted to the "trig" list each time?
                            # Take a look at Steps 1 to 3 shown in the above blocks of comment.  
                            # They are the index indicating where the item is inserted in the updated "trig" list.         
print(trig)
