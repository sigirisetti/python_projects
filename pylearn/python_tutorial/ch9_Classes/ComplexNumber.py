class ComplexNumber:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

x = ComplexNumber(3.0, -4.5)

print(x.r, x.i)