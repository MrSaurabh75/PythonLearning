# Oprator overloading:
class Vector:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def __str__(self):
        return f"{self.x}i + {self.y}j + {self.z}k"
    def __add__(self,i):
        return f"{self.x+i.x}i + {self.y+i.y}j + {self.z+i.z}k"
v1 = Vector(3,4,5)
print(v1)
v2 = Vector(3,4,5)
print(v2)

print(v1+v2)