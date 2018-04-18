class MyClass:
    """A simple example class"""
    i = 12345

    def __init__(self):
        print('MyClass Constructor')

    def f(self):
        return 'hello world'


x = MyClass()
print(x.f())

# Data attributes need not be declared; like local variables,
# they spring into existence when they are first assigned to
x.counter = 1

while x.counter < 10 :
    x.counter *= 2
print(x.counter)

del x.counter