def squareroot(n):
    a=0.5*n
    b=0.5*(a+n/a)
    while b!=a:
        a=b
        b=0.5*(a+n/a)
    return round(a,1) 
number=float(input("Enter a positive number: "))  
squareroot(number)
print(f"The square root of {number} is approx. {squareroot(number)}.")
