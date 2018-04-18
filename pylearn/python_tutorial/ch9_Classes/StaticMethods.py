class Car(object):

    def __init__(self, model, make):
        self.model = model
        self.make = make

    @staticmethod
    def drive(self):
        print("driving")

    def printModelNMake(self):
        print("Model %s and Make %s" % (self.model, self.make))


c = Car("ABC", 1977)
c.drive()
c.printModelNMake()


