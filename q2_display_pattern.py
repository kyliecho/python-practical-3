# Displaying patterns

n = int(input("Enter your integer: "))

for i in range (n,0,-1):
    print((i-1)*"\t",end="")
    for k in range(n-i+1,0,-1):
        print(k,end="\t")
    print()

