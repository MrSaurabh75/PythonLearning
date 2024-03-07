# Getters and Setters : Using getter you can able to use the retturn value of function as object property and using setters you can set the value
class MyClass:
    def __init__(self,value):
        self._value=value
    def show(self):
        print(f"{self._value}")
    @property
    def ten_value(self):
        return 10*self._value

    @ten_value.setter
    def ten_value(self,new_value):
        self._value=new_value/10

obj = MyClass(10)
obj.ten_value=67
print(obj.ten_value)
obj.show()