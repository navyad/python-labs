class A:
    def who_am_i(self):
        print("I am a A")

    def call_me(self):
        print("call_me A")

class B(A):
    def who_am_i(self):
        print("I am a B")

class C(A):
    def who_am_i(self):
        print("I am a C")
    def call_me(self):
        print("call_me C")

class D(B,C):
    def who_am_i(self):
        print("I am a D")

d1 = D()
d1.who_am_i()
d1.call_me()
print(D.mro())
