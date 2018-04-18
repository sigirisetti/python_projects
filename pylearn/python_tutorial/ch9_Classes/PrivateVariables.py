class Mapping:
    def __init__(self, iterable):
        print('Mapping')
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    def get_items(self):
        return self.items_list

    __update = update   # private copy of original update() method


class MappingSubclass(Mapping):

    def __init__(self):
        super().__init__([]) # call super class
        print('Mapping Subclass')

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)


obj = MappingSubclass()
obj.update(["k1", "k2"], ["v1", "v2"])
print(obj.getItems())