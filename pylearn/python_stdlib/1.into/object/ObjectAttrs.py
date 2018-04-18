class Animal:

    # Python will call this method whenever you request an attribute that hasn't already been defined, so you can define what to do with it.
    def __getattr__(self, name):
        print("In __getattr__(%s)" % name)
        return "<<NA>>"

    # If you need to catch every attribute regardless whether it exists or not, use __getattribute__ instead.
    # The difference is that __getattr__ only gets called for attributes that don't actually exist.
    # If you set an attribute directly, referencing that attribute will retrieve it without calling __getattr__
    def __getattribute__(self, attr):
        print("In __getattribute__(%s)" % attr)
        try:
            return super(Animal, self).__getattribute__(attr)
        except KeyError:
            print("No key : %s" % attr)


a = Animal()
a.name = "Tiger"
print(a.name)
print(a.species)
print(dir(a))
print(a.__slots__)
