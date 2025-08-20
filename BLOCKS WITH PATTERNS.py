blocks=int(input("Enter number of blocks: "))
lines=int(input("Enter number of lines: "))
stars=int(input("Enter numkber of stars: "))
for i in range (blocks):
    count=0
    for j in range(lines-i):
        for k in range(stars):
            print('*',end=" ")
            count+=1
        print()
    print(count)
    print("___________________")