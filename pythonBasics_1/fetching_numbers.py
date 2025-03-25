
s= "a1b2bb3v4c5"

numbers=[]
for i in s:
    print(i.isdigit())
    if i.isdigit()=="True":
        numbers.append(i)
print(numbers)