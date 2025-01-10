values = [1, 2, "Rahul", 4, 5.5]

print(values[0])
print(values[3])
print(values[-1])
print(values[1:4])
values.insert(3, "Shetty")
print(values)
values.append("End")
print(values)
values[2] = "RAHUL"
del values[0]
print(values)

val = (1, 2, "Rahul", 4.5)
print(val[2])
# val[2]="Rahul"

dic = {"a": 2, 4: "abc", "c": "Hello"}
print(dic[4])
