

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    zero=0
    positive=0
    negative=0
    num=len(arr)

    for i in arr:
        if i > 0:
            positive = positive + 1
        elif i < 0:
            negative = negative + 1
        else:
            zero = zero +1
    positive_proportion=positive/num
    negative_proportion=negative/num
    zero_proportion= zero/num
    print(f"{positive_proportion:.6f}")
    print(f"{negative_proportion:.6f}")
    print(f"{zero_proportion:.6f}")

if __name__ != '__main__':
    pass
else:
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
