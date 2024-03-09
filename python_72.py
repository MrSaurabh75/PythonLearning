# Super Keyword : super() keyword is used to refer to the parent class method
class A:
    def parent_method(self):
        print("Parent Method")
class B(A):
    # def parent_method(self):
    #     print("Saurabh")
    def child_method(self):
        print("Child method")
        super().parent_method()
b = B()
b.child_method()
b.parent_method()