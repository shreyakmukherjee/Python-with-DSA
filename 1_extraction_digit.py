'''
After extrction of a digit from a number we can do-
--count numbers
--reverse the number
--check palindrome
--check armstrong
etc..
'''
# Count th digits and display those digits extracted from the number 

n = int(input("Enter the number: "))
count = 0
print("number is",n)
print("Digits are: ")
while(n>0):
    digit = n%10
    count = count +1
    print(digit)
    n = n//10

print("The total digits present in this number is: ", count)