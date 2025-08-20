n = 1
total = 0
while n != 0:
    n = int(input("Enter the number: "))
    if n == 0:
        break
    if n < 40 or n > 100:   
        continue
    total += n   
print( total)