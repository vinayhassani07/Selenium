from oopsdemo import Calculator


class Childimp(Calculator):
    num2 = 200

    def __init__(self):
        Calculator.__init__(self)

    def getCompleteData(self):
        return self.num2 + self.num + self.Summation()


obj = Childimp(5, 10)
print(obj.getCompleteData())
