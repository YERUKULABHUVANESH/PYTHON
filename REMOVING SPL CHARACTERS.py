x = (input("Enter any string: "))
result1=""
for i in x:
    if i.isalpha():
        result1=result1+i
    
    result=result1.capitalize()
print(result)