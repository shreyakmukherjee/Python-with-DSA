from math import *
n = int(input("Enter the number: "))
temp = n
count = 0
while temp>0:
    count +=1
    temp=temp//10

print (f"The number of digits in {n} is:",count)


# print(int(log10(n)+1))
# for this math import is required