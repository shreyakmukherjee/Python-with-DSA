'''
After extrction of a digit from a number we can do-
--count numbers
--reverse the number
--check palindrome
--check armstrong
etc..
'''
# Display the digits extracted from the number 

n = int(input("Enter the number: "))
print("number is",n)
print("Digits are: ")
while(n>0):
    digit = n%10
    print(digit)
    n = n//10

