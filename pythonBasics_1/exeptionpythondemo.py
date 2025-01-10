item = 0

# if item != 2:
#     pass
    # raise Exception("Item not match ")

# assert (item == 2)

try:
    with open("filelog.txt") as  reader:
        print(reader.read())

except Exception as e:
    print(e)

finally:
    print("this is finally ")

