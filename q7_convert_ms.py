# Converting milliseconds to hours, minutes, and seconds

n = int(input("Enter milliseconds: "))

def convert_ms(n):
    h = n // 3600000
    m = (n % 3600000) // 60000
    s = ((n % 3600000) % 60000) // 1000
    print(f'{h}:{m}:{s}')

convert_ms(n)
