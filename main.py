class Grandparent:
    age = 60


class Parent(Grandparent):
    age = 50

class Son(Parent):
    age = 30
babusy = Parent()
anya = (Son)
print(babusy.age)
print(anya.age)
