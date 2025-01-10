class Calculator:
    num = 100

    def __init__(self, a, b):
        print("I am called automatically when obj is created ")
        self.a = a
        self.b = b

    def getData(self):
        print("I am in get data function ")

    def Summation(self):
        return self.a + self.b + self.num


obj = Calculator(2, 3)
obj.getData()
print(obj.Summation())
