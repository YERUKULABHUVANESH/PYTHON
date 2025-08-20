a=int(input("Enter any number: "))
b=int(input("Enter any number: "))
while(b!=0):
    rem=a%b
    a=b
    b=rem
print(a)