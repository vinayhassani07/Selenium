def swap_case(s):
    str=""
    for i in s:
        if i == i.lower():
            u= i.upper()
            str=str + u
        elif i == i.upper():
            l= i.lower()
            str = str + l
    return str



if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
