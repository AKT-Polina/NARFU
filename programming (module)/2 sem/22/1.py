import unittest as u
import uuid

class testPony(u.TestCase):
    
    # Метод для проверки имени пони
    def test_name(self):
        p = pony("Sparkle", 4)
        self.assertEqual(p.name, "Sparkle")
        
    # Метод для проверки возраста пони
    def test_age(self):
        p = pony(age=6)
        self.assertEqual(p.age, 6)
        
    # Метод для проверки значений по умолчанию
    def test_default_values(self):
        p = pony()
        self.assertEqual(p.name, "Noname")
        self.assertEqual(p.age, 0)

class pony:
    id: str = None
    
    def __init__(self, name="Noname", age=0):
        self.name = name
        self.age = age
        if not self.id:
            self.id = str(uuid.uuid4())

        
    def __str__(self):
        return 'Имя: {0}, Возраст: {1}'.format(self.name, self.age)

    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age
        
if __name__ == "__main__":
    p1 = pony("Рарити", 22)
    print("Идентефикатор: ")
    print(p1.id)
    print("Иформация о пони: ")
    print(p1.__str__())
    p2 = pony()
    print("Иформация о пони: ")
    print(p2.__str__())

    u.main()
    
    

