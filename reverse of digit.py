#find the reverse of digit.
n=int(input("Enter a digit:"))
reverse=0
while n>0:
    r=n%10
    reverse=reverse*10+r
    n=n//10
print(" The reverse digit is",reverse)
input()
    
    
