from datetime import datetime
import pickle
import unittest
import gc

class testUnicorn(unittest.TestCase):

    # Метод для проверки имени пони
    def test_name(self):
        p = unicorn("Sparkle", 4)
        self.assertEqual(p.name, "Sparkle")
        
    # Метод для проверки возраста пони
    def test_age(self):
        p = unicorn(age=6)
        self.assertEqual(p.age, 6)

    # Метод для проверки магии пони
    def test_magic(self):
        p = unicorn()
        self.assertEqual(p.magic_power, True)

class testPegasus(unittest.TestCase):

    # Метод для проверки имени пони
    def test_name(self):
        p = pegasus("Sparkle", 4)
        self.assertEqual(p.name, "Sparkle")
        
    # Метод для проверки возраста пони
    def test_age(self):
        p = pegasus(age=6)
        self.assertEqual(p.age, 6)

    # Метод для проверки магии пони
    def test_magic(self):
        p = pegasus()
        self.assertEqual(p.can_fly, True)
    
    


class pony:
    
    def __init__(self, name="Noname", age=0):
        self.name = name
        self.age = age        

    
    def __del__(self):
        print(f"Пони {self.name} был удален.")
        
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

class unicorn(pony):
    def __init__(self, name="Noname", age=0, magic_power=True):
        super().__init__(name, age)
        self.magic_power = magic_power

    def use_magic(self):
        if self.magic_power:
            print(f"{self.name} ипользует магию!")
        else:
            print(f"{self.name} не может использовать магию.")
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def get_use_magic(self):
        return self.use_magic

    def set_use_magic(self, use_magic):
        self.use_magic = use_magic
    

class pegasus(pony):
    def __init__(self, name="Noname", age=0, can_fly=True):
        super().__init__(name, age)
        self.can_fly = can_fly

    def flight(self):
        if self.can_fly:
            print(f"{self.name} летит!")
        else:
            print(f"{self.name} не может летать.")
            
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def get_can_fly(self):
        return self.can_fly

    def set_can_fly(self, can_fly):
        self.can_fly = can_fly

if __name__ == "__main__":
    
    u = unicorn(name="Твайлайт Спаркл", age=18, magic_power=True)
    u.use_magic()
    print("Имя пони: ",u.get_name())
    u.set_name("Рарити")
    print("Имя пони: ",u.get_name())
    u.set_use_magic(False)
    print(u.get_use_magic())
    peg = pegasus(name="Флаттершай", age=18, can_fly=False)
    peg.flight()
    peg.set_can_fly(True)
    peg.flight()

    unittest.main()
  
    
    

