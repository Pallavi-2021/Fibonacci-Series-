#FIBONACCI SERIES
n= int(input("enter the range:"))
n1=0
n2=1
i=2
print("The fibonacci series:")
if n<0:
    print("Please enter a value greater than zero")
elif n==1:
    print(n1)
else:    
    print(n1)
    print(n2)
    while i<n:
        n3=n1+n2
        print(n3)
        n1=n2
        n2=n3
        i=i+1
        
    
