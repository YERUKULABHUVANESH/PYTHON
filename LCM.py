a=int(input("Enter any num1:"))
b=int(input("Enter any num2:"))
if a>b:
    big=a
else:
    big=b
step=big
while(True):
    if big%a==0 and big%b==0:
        break
    else:
        big=big+step
print("The LCM of", a, "and", b, "is", big)