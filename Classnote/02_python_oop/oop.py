import os
os.system('cls' if os.name=="nt" else 'clear')
# ---------------------------------------------
# ---------------------------------------------
# Python - OOP
# ---------------------------------------------
# Object Oriented Programming
# Classes -> BluePrint: Mimarların kullandığı mavi şablon kağıdıdır. Obje orada tanımlanmıştır.
# DRY: Don't Repeat Yourself
# ---------------------------------------------
# ---------------------------------------------
'''
def print_type(data):
    for per in data:
        print(per, type(per))

print_type(['Qadir', 22, 22.3, [1,2,3], True, (1,2,3), lambda x:x])
'''
# ---------------------------------------------
'''
#  Python'da class oluşturma:
class ClassName: # PEP8 -> PascalCase yapıda isimlendirilir: ExampleMyClassName
    # Attributes/Properties
    variable_for_class = 'value'
    # Wrong Using:
    # if ()...
    # Methods(arguments/parameters):
    def example_function(): # PEP8 -> snake_case yapıda isimlendirilir: example_my_function_name()
        # Parameters:
        variable_for_function = 'value'
        # Conditions:
        # if () ....
'''
# ---------------------------------------------
'''
class Person:
    name = 'Qadir'
    surname = 'Adamson'

print(Person)
print(Person.name)
print(Person.surname)

# Set Object from Class:
personal_1 = Person() # Instance

print(personal_1)
print(personal_1.name)
print(personal_1.surname)

print('----------------')

personal_1.name = 'Mevlüt'
personal_1.surname = 'M'
print(personal_1.name)
print(personal_1.surname)
print(Person.name)
print(Person.surname)

print('----------------')

personal_1.path = 'FullStack'
print(personal_1.path)
# print(Person.path) # Instance ile oluşturulan attr orjinal class'ı değiştirmez.

print('----------------')

personal_2 = Person()
print(personal_2)
personal_2.location = 'Germany'
print(personal_2.location)
# print(personal_1.location) # Bir instance ile oluşturulan attr başka bir instance'i etkilemez.
print(personal_2.name)
print(personal_1.name)
'''

# ---------------------------------------------
'''
# SELF keyword:
class Person:
    name = 'Qadir'
    surname = 'Adamson'
    # Method:
    # this -> self
    def test(self):
        print(self.name)

person3 = Person()
# Call Method:
person3.test() # <- run like this on backgound: Person.test(person3)
'''
# ---------------------------------------------
'''
# Getter & Setter Methods:
class Person:
    # Underscore ile başlayan değişkenlerin instance tarafında çağırlmaması/değiştirilmemesi beklenir.
    # Piyasa standartıdır. Çağrılabilir.
    _name = 'Qadir' 
    _surname = 'Adamson'
    # Double-Underscore ile başlayan değişkenleri dışardan çağrılmasını engeller.
    __location = 'Germany' # <- Encapsullation

    # Getter Method:
    def get_name(self):
        # ...
        return self._name + ' ' + self._surname + ' ' + self.__location

    # Setter Method:
    def set_name(self, new_name, new_surname, new_location):
        # ...
        self._name = new_name
        self._surname = new_surname
        self.__location = new_location

person4 = Person() # Instance oluşturma -> Abstaction örneğidir.
# person4._name = 'Henry' # Dont use.
# print(person4._name) # Dont use.
# print(person4.__location) # Dont calling.
print(person4.get_name())
person4.set_name('Henry', 'Forester', 'Turkey')
print(person4.get_name())
'''
# ---------------------------------------------
'''
# Static Methods:
class Person:
    name = 'Qadir'
    surname = 'Adamson'
    # Method:
    # this -> self
    def test(self):
        print(self.name)
    
    @staticmethod
    def static_method():
        print('Hello')

person5 = Person()
person5.test()
person5.static_method()
'''
# ---------------------------------------------
'''
# Constructor Methods:
class Person:
    name = 'Qadir'
    surname = 'Adamson'

    # Dunder Methods -> __method__()

    # Constructor Method: __init__()
    def __init__(self):
        print('CLass Çağrıldı.')

    # Varsayılan yazılacak veri __str__ ile belirlenir.
    # Intance için geçerlidir.
    def __str__(self):
        return self.name + ' ' + self.surname

# print(Person)
person6 = Person() # Bu aşamada __init__() otomatik çalışır.
print(person6)
'''
# ---------------------------------------------
# Encapsulation and Abstraction: Gizleme (kapsülleme) ve Soyutlama:
# Encapsulation: Protected, Private değişkenler gibi değişmeyen/erişilmeyen değişkenlerin kullanılması.
# Abstraction: Kodların gizliliği.
# ---------------------------------------------
# Inheritance and Polymorphism
# Inheritance: Bir sınıfı başka bir sınınfın özellikleri ile birlikte çağırma (miras alma)
# Polymorphism: Miras aldığımız sınıfın özellik/methodlarını değiştirebilme, yeniden yazma.
# ---------------------------------------------

class Person:
    name = 'Qadir'
    surname = 'Adamson'

    def get_name(self):
        return self.name + ' ' + self.surname

    def set_name(self, name, surname):
        self.name = name
        self.surname = surname

class Department:
    department = 'FullStack'

    def set_department(self, department):
        self.department = department

class Employee(Person, Department): # Inheritance
    salary = 5000

    # Miras aldığımız methodu yeniden tanımlayarak, öncekini iptal etmiş olduk
    # Bu işleme Override denir.
    def set_name(self, name, surname, salary, department):
        # super() -> ilk inherit edilen classı temsil eder.
        super().set_name(name, surname) # super() kullanımında self belirtmeye gerek yoktur.
        # Department.department = department
        Department.set_department(self, department) # İlk olandan sonraki class inheritler super ile çağılmaz, self kullanılması gerekir.
        self.salary = salary

    def get_name(self):
        return self.name + ' ' + self.surname + ' ' + str(self.salary) + ' ' + self.department

employee = Employee()
print(employee.name)
print(employee.get_name())
print(employee.salary)
employee.set_name('Victor', 'Hugo', 10000, 'AWS')
print(employee.salary)
print(employee.get_name())


# ---------------------------------------------
'''
# Overload: Kullanılmıyor.
from multimethods import multimethod
class NewClass(Department):
    @overload(str, str, str)
    def set_department(self, department, extra_parameter):
        return department + ' ' + extra_parameter
'''
# ---------------------------------------------