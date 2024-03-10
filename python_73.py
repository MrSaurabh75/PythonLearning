# Magic/Dunder Method
# __len__():
class Employee:
    name="Saurabh"
    def __len__(self):
        i=0
        for item in self.name:
            i=i+1
        return i
e = Employee()
print(e.name)
print(len(e))