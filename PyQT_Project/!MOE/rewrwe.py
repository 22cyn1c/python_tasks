class A:
    def method(self, x, y):
        print(x + y)

class B:
    def call_a(self):
        A.method(self, 1, 2)

b = B()
b.call_a()