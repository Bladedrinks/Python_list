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
    i += 2
    trig.insert(i, item)
    # print(trig)
print(trig)
