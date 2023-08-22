#Ichsan Ardika Akbar
#SMKDEV Challenge advance

# 5 4 3 2 1
# 4 3 2 1
# 3 2 1 
# 2 1 
# 1
# Write a program to use for loop to print the following reverse number pattern

for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()