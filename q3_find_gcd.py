# Computing GCD

m = int(input("Enter first integer: "))
n = int(input("Enter second integer: "))

def gcd(m,n):
    d = min(m,n)
    while (m % d == 0 and n % d == 0) is False:
        d -= 1
    print("The greatest common divisor is",d)

gcd(m,n)
