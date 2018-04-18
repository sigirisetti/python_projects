s1 = set([1,2,3,4,4,4,5,5,5,6,6])
print(len(s1))

class Person(object):

    def __init__(self, id, name):
        self.id = id
        self.name = name

    # this only and any contained objects. More descriptive
    def __str__(self):
        return "id = %d and name = %s" % (self.id, self.name)

    # Only this object
    def __repr__(self):
        return "id = %d" % self.id

    def __eq__(self, other):
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)


p1 = Person(1, "Sri")
p2 = Person(1, "Prakhya")
p3 = Person(2, "Surya")
p4 = Person(3, "Appu")
p5 = Person(4, "other")

# Need to implement both "__eq__" and "__hash__" for objects to be used properly in set()
persons = set([p1,p2,p3,p4,p5])

print("person length %d" % len(persons))

for p in persons:
    print(p)
