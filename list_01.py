# Program to create a list consisting of powers of 2 (like this: 1, 2, 4, 8, 16, ..., 512,
# using the for loop and the list.append() method.

# power of 2 is 2 ** x, where x represents the exponents which ranges from 0 to 10 (10 excluded).
# Each time we pick an integer from the integer range from 0 to 10 (that is, 0, 1, 2, ..., 8, 9)
# and then assign it to x as in the algebraic expression. Finally, we will be getting
# 2 ** 0 == 1
# 2 ** 1 == 2
# 2 ** 2 == 4
# 2 ** 3 == 8
# 2 ** 4 == 16
# 2 ** 5 == 32
# 2 ** x == (2 raised to the power of x)
# 2 ** 9 == 512
# The question is how to put them together in the ascending order. We can associate it with the method for finding the
# sum of a number sequence using for loop and the += assignment operator. The list method that may correspond to the +=
# assignment operator is the list.append() method.
# x = 0  (Assign 0 to the variable x, which is the starting point)
# x += 1 or x = x + 1 where x has been set to  0 in the above line, then we get x = 1
# x += 2 or x = x + 2 where x has been set to  1 in the above line, then we get x = 3
# x += 3 or x = x + 3 where x has been set to  3 in the above line, then we get x = 6
# x += 4 or x = x + 4 where x has been set to  6 in the above line, then we get x = 10
# x += 5 or x = x + 5 where x has been set to 10 in the above line, then we get x = 15
# ...
# In the same way, we can create an empty list [] which corresponds to the 0 in the above example as the starting point
# and then use the list.append() method to add each new item to the list.
num_seq = []
for x in range(10):
    num_seq.append(2 ** x)
print(num_seq)













