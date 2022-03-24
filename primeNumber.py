n = 3

# taking the input
#n= int(input())

# define a flag variable
flag = False

# prime numbers are greater than 1
if n > 1:
# check for factors
    for i in range(2, n):
        if (n % i) == 0:
# if factor is found, set flag to True
            flag = True
# break out of loop
            break

# check if flag is True
if flag:
    print(n, "is not an prime number") 
else:
    print(n, "is  an prime number")