# Displaying matrix of 0s and 1s

import random

x = int(input("Enter a positive integer: "))

def print_matrix(n):
        matrix = []
        for i in range(0, n*n):
                i = random.randint(0, 1)
                matrix.append(str(i))
        for i in range(0, x*x, x):
                print(" ".join(matrix[i:i+x]))

print_matrix(x)




