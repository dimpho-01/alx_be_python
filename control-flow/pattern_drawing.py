size = int(input("Enter the size of the pattern:"))

counter = 1
while counter <= size:
    for j in range(1,size + 1):
        print("*", end="")
    print()
    counter+= 1