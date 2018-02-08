# Displaying an integer reversed

def reverse_int(n):
    r = 0
    while n > 0:
        r *= 10
        r += n % 10
        n //= 10
    return r

n = int(input("Enter number: "))
print(reverse_int(n))
