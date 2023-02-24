class A:
    def whoami(self):
        print('i am in A')
class B(A):
    def whoami(self):
        print('i am in B')
class C(A):
    def whoami(self):
        print('i am in C')
class D(B,C):
    pass

d1=D()
d1.whoami()

#METHOD RESOLUTION ORDER