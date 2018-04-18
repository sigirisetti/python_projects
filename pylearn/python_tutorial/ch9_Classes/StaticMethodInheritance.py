class Base(object):
    @staticmethod
    def foo():
        print("Base.foo()")

    def bar(self):
        print("Base.bar()")

    @classmethod
    def baz(cls):
	    print("Base.baz()")


class Derived (Base):

    def bar(self):
        print("Derived.bar()")

b = Derived()

b.foo()
b.bar()
b.baz()
