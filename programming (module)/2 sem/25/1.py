from datetime import datetime
import pickle
import unittest
import gc

class pony:
    
    def __init__(self, name="Noname", age=0):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Имя не может содержать цифры")
        else:
            self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if(value >= 100):
            raise ValueError("Пони столько не живут")
        else:
            self.__age = value

class unicorn(pony):
    def __init__(self, name="Noname", age=0, magic_power=True):
        super().__init__(name, age)
        self.__magic_power = magic_power

    @property
    def magic_power(self):
        return self.__magic_power

    @magic_power.setter
    def magic_power(self, value):
        self.__magic_power = value

    def use_magic(self):
        if self.__magic_power:
            print(f"{self.name} ипользует магию!")
        else:
            print(f"{self.name} не может использовать магию.")


class pegasus(pony):
    def __init__(self, name="Noname", age=0, can_fly=True):
        super().__init__(name, age)
        self.__can_fly = can_fly

    @property
    def can_fly(self):
        return self.__can_fly

    @can_fly.setter
    def can_fly(self, value):
        self.__can_fly = value

    def flight(self):
        if self.__can_fly:
            print(f"{self.name} летит!")
        else:
            print(f"{self.name} не может летать.")
    
class TestPony(unittest.TestCase):
    def setUp(self):
        self.p = pony("Sparkle", 4)

    def test_valid_name_setter(self):
        self.p.name = "Rainbow Dash"
        self.assertEqual(self.p.name, "Rainbow Dash")

    def test_invalid_name_setter(self):
        with self.assertRaises(TypeError):
            self.p.name = 123


    def test_valid_age_setter(self):
        self.p.age = 12
        self.assertEqual(self.p.age, 12)

    def test_invalid_age_setter(self):
        with self.assertRaises(ValueError):
            self.p.age = 1234 


if __name__ == "__main__":
    
    u = unicorn("Твайлайт Спаркл", 18,True)
    print(u.age)
    #Error
    #u.age = 1000
    u.age = 10
    print(u.age)

    print(u.name)
    #Error
    #u.name = 122121
    u.name = "New name"
    print(u.name)
    
    u.use_magic()
    u = pegasus("Рейнбоу Дэш", 18,True)
    u.flight()

    unittest.main()
    
  
    
    
##class testUnicorn(unittest.TestCase):
##
##    # Метод для проверки имени пони
##    def test___name(self):
##        p = unicorn("Sparkle", 4)
##        self.assertEqual(p.__name, "Sparkle")
##        
##    # Метод для проверки возраста пони
##    def test___age(self):
##        p = unicorn(__age=6)
##        self.assertEqual(p.__age, 6)
##
##    # Метод для проверки магии пони
##    def test_magic(self):
##        p = unicorn()
##        self.assertEqual(p.__magic_power, True)
##
##class testPegasus(unittest.TestCase):
##
##    # Метод для проверки имени пони
##    def test___name(self):
##        p = pegasus("Sparkle", 4)
##        self.assertEqual(p.__name, "Sparkle")
##        
##    # Метод для проверки возраста пони
##    def test___age(self):
##        p = pegasus(__age=6)
##        self.assertEqual(p.__age, 6)
##
##    # Метод для проверки магии пони
##    def test_magic(self):
##        p = pegasus()
##        self.assertEqual(p.__can_fly, True)
##    

