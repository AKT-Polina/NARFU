from datetime import datetime
import pickle
import unittest
import gc

class pony:
    """
    Класс, представляющий пони.

    Атрибуты:
        name (str): Имя пони.
        age (int): Возраст пони.

    Методы:
        __add__(other): Операция сложения.
        __sub__(other): Операция вычитания.
        __mul__(other): Операция умножения.
        __truediv__(other): Операция деления.
        __str__(): Представление объекта в виде строки.
    """
    def __init__(self, name="Noname", age=0):
        """
        Конструктор класса Pony.

        Параметры:
            name (str): Имя пони. По умолчанию "Noname".
            age (int): Возраст пони. По умолчанию 0.
        """
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
    
    def __str__(self):
        return 'Имя: {0}, Возраст: {1}'.format(self.name, self.age)

    #####
    def __add__(self, other):
        """Операция сложения"""
        if isinstance(other, pony):
            return pony(name=self.name + ' & ' + other.name, age=self.age + other.age)
        elif isinstance(other, int):
            return pony(name=self.name, age=self.age + other)
        else:
            raise TypeError("Неподдерживаемый тип для сложения")

    def __sub__(self, other):
        """Операция вычитания"""
        if isinstance(other, pony):
            return pony(name=self.name + ' & ' + other.name, age=self.age - other.age)
        elif isinstance(other, int):
            return pony(name=self.name, age=self.age - other)
        else:
            raise TypeError("Неподдерживаемый тип для вычитания")

    def __mul__(self, other):
        """Операция умножения"""
        if isinstance(other, int):
            return pony(name=self.name * other, age=self.age * other)
        else:
            raise TypeError("Неподдерживаемый тип для умножения")

    def __truediv__(self, other):
        """Операция деления"""
        if isinstance(other, int):
            return pony(name=self.name, age=self.age // other)
        else:
            raise TypeError("Неподдерживаемый тип для деления")


    

class unicorn(pony):
    """
        Класс, представляющий единорога. Наследник класса pony

        Атрибуты:
            name (str): Имя единорога.
            age (int): Возраст единорога.
            magic_power (bool): Возможность использовать магию

        Методы:
            use_magic(): Использование магии
    """
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
        """Использование магии"""
        if self.__magic_power:
            print(f"{self.name} ипользует магию!")
        else:
            print(f"{self.name} не может использовать магию.")


class pegasus(pony):
    """
    Класс, представляющий пегаса. Наследник класса pony

    Атрибуты:
        name (str): Имя пегаса.
        age (int): Возраст пегаса.
        magic_power (bool): Возможность летать

    Методы:
        use_magic(): Полет
    """
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
        """Полет"""
        if self.__can_fly:
            print(f"{self.name} летит!")
        else:
            print(f"{self.name} не может летать.")
    
class TestPonyArithmetic(unittest.TestCase):
    def setUp(self):
        self.pony1 = pony("Sparkle", 4)
        self.pony2 = pony("Twilight", 8)    

    def test_add_incorrect_type(self):
        with self.assertRaises(TypeError):
            self.pony1 + "invalid type"

    def test_subtract_incorrect_type(self):
        with self.assertRaises(TypeError):
            self.pony1 - "invalid type"

    def test_multiply_incorrect_type(self):
        with self.assertRaises(TypeError):
            self.pony1 * "invalid type"

    def test_divide_incorrect_type(self):
        with self.assertRaises(TypeError):
            self.pony1 / "invalid type"


if __name__ == "__main__":
    
    pony1 = pony("Sparkle", 4)
    pony2 = pony("Twilight", 8)

    result_add = pony1 + pony2
    print(result_add.__str__())

    result_sub = pony2 - pony1
    print(result_sub.__str__())

    result_mul = pony1 * 2
    print(result_mul.__str__())

    result_div = pony2 / 2
    print(result_div.__str__())
    
    print(result_div.__str__().__doc__)

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

