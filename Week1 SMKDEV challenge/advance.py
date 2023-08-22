#Ichsan Ardika Akbar
#SMKDEV Challenge advance

# 5 4 3 2 1
# 4 3 2 1
# 3 2 1 
# 2 1 
# 1
# Write a program to use for loop to print the following reverse number pattern

for i in range(5, 0, -1):            # for loop to initialize row
    for j in range(i, 0, -1):        # for loop to initialize column
        print(j, end=" ")            # print the number(s)
    print()                          # end the column, so we have a new row
