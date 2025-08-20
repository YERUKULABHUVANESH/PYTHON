string=str(input("Enter any string : "))
words=string.split()
print("No of words in a string is:",len(words))

string=str(input("Enter any string : "))
count = 1   
for char in string:
    if char == " ":   
        count += 1
print("Number of words:", count)