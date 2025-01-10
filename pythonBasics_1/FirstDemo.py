# print("Hello ")
# a = 3
# print(a)
# str1 = "Hello World"
# print(str1)
# b, c, d = 5, 6.5, "green"
# # print("Value is " + b)
# print("{} {}".format("Value is", b))
# print("Value is " + str(b))
# print(type(b))
# print(type(c))


ar_count = int(input().strip())

ar = list(map(int, input().rstrip().split()))


def aVeryBigSum(ar):
    s=sum(ar)
    return s


result= aVeryBigSum(ar)
print(result)
# 5
# 1000000001 1000000002 1000000003 1000000004 1000000005