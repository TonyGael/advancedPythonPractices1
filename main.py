# class Person:
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __del__(self):
#         print("Object is being deconstructed!")
#
#
# p = Person("Tony", 33)

class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    '''
        def __add__(self, other):
        Este método especial permite sumar dos vectores. Toma otro objeto de la clase Vector como argumento (other).
        Devuelve un nuevo objeto Vector cuyas componentes x y y son la suma de las componentes correspondientes del
        objeto actual (self) y el objeto other.
    '''
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"x: {self.x}, y: {self.y}"

    def __call__(self):
        print('I was call with __call__, method overwriting')


v1 = Vector(10, 20)
v2 = Vector(50, 60)
v3 = v1 + v2
print(v3) # unless we change the representation method the result obtainded is: <__main__>.Vector object at 0X... something

print(v3.x)
print(v3.y)
print("v3: ", v3)

v3()
