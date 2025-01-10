def swap_case(s):
    strrr = ""
    for i in s:
        if i == i.lower():
            u = i.upper()
            strrr = strrr + u
        elif i == i.upper():
            l = i.lower()
            strrr = strrr + l
    return strrr


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
