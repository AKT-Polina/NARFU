import unittest

class Pony:
    def __init__(self, name="Noname", age=0):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Имя: {self.name}, Возраст: {self.age}'

class Unicorn(Pony):
    def __init__(self, name="Noname", age=0, magic_power=True):
        super().__init__(name, age)
        self.magic_power = magic_power

    def use_magic(self):
        if self.magic_power:
            print(f"{self.name} использует магию!")
        else:
            print(f"{self.name} не может использовать магию.")

class Pegasus(Pony):
    def __init__(self, name="Noname", age=0, can_fly=True):
        super().__init__(name, age)
        self.can_fly = can_fly

    def flight(self):
        if self.can_fly:
            print(f"{self.name} летит!")
        else:
            print(f"{self.name} не может летать.")

# Массивы для хранения данных
ponies = []
unicorns = []
pegasi = []

def add_entity():
    print("Какой тип сущности вы хотите добавить?")
    print("1. Пони")
    print("2. Единорог")
    print("3. Пегас\n")

    entity_choice = input("Ваш выбор: ")

    if entity_choice == '1':
        name = input("Введите имя пони: ")
        age = int(input("Введите возраст пони: "))
        
        new_pony = Pony(name, age)
        ponies.append(new_pony)
        print(f"Пони {new_pony.name} успешно добавлен!\n")
    elif entity_choice == '2':
        name = input("Введите имя единорога: ")
        age = int(input("Введите возраст единорога: "))
        magic_power = True
        
        new_unicorn = Unicorn(name, age, magic_power)
        unicorns.append(new_unicorn)
        print(f"Единорог {new_unicorn.name} успешно добавлен!\n")
    elif entity_choice == '3':
        name = input("Введите имя пегаса: ")
        age = int(input("Введите возраст пегаса: "))
        can_fly = True
        
        new_pegasus = Pegasus(name, age, can_fly)
        pegasi.append(new_pegasus)
        print(f"Пегас {new_pegasus.name} успешно добавлен!\n")
    else:
        print("Неверный выбор. Попробуйте снова.\n")
        add_entity()

def change_entity():
    print("Какой тип сущности вы хотите изменить?")
    print("1. Пони")
    print("2. Единорог")
    print("3. Пегас\n")

    entity_choice = input("Ваш выбор: ")

    if entity_choice == '1':
        name = input("Введите имя пони, которого вы хотите изменить: ")
        index = find_index(ponies, 'name', name)
        if index != -1:
            new_name = input("Введите новое имя пони: ")
            new_age = int(input("Введите новый возраст пони: "))
            ponies[index].name = new_name
            ponies[index].age = new_age
            print(f"Информация о пони {new_name} была успешно обновлена!\n")
        else:
            print(f"Пони {name} не найден.\n")
    elif entity_choice == '2':
        name = input("Введите имя единорога, которого вы хотите изменить: ")
        index = find_index(unicorns, 'name', name)
        if index != -1:
            new_name = input("Введите новое имя единорога: ")
            new_age = int(input("Введите новый возраст единорога: "))
            unicorns[index].name = new_name
            unicorns[index].age = new_age
            print(f"Информация о единороге {new_name} была успешно обновлена!\n")
        else:
            print(f"Единорог {name} не найден.\n")
    elif entity_choice == '3':
        name = input("Введите имя пегаса, которого вы хотите изменить: ")
        index = find_index(pegasi, 'name', name)
        if index != -1:
            new_name = input("Введите новое имя пегаса: ")
            new_age = int(input("Введите новый возраст пегаса: "))
            pegasi[index].name = new_name
            pegasi[index].age = new_age
            print(f"Информация о пегасе {new_name} была успешно обновлена!\n")
        else:
            print(f"Пегас {name} не найден.\n")
    else:
        print("Неверный выбор. Попробуйте снова.\n")
        change_entity()

def delete_entity():
    print("Какой тип сущности вы хотите удалить?")
    print("1. Пони")
    print("2. Единорог")
    print("3. Пегас\n")

    entity_choice = input("Ваш выбор: ")

    if entity_choice == '1':
        name = input("Введите имя пони, которого вы хотите удалить: ")
        index = find_index(ponies, 'name', name)
        if index != -1:
            del ponies[index]
            print(f"Пони {name} был успешно удален.\n")
        else:
            print(f"Пони {name} не найден.\n")
    elif entity_choice == '2':
        name = input("Введите имя единорога, которого вы хотите удалить: ")
        index = find_index(unicorns, 'name', name)
        if index != -1:
            del unicorns[index]
            print(f"Единорог {name} был успешно удален.\n")
        else:
            print(f"Единорог {name} не найден.\n")
    elif entity_choice == '3':
        name = input("Введите имя пегаса, которого вы хотите удалить: ")
        index = find_index(pegasi, 'name', name)
        if index != -1:
            del pegasi[index]
            print(f"Пегас {name} был успешно удален.\n")
        else:
            print(f"Пегас {name} не найден.\n")
    else:
        print("Неверный выбор. Попробуйте снова.\n")
        delete_entity()

def view_entities():
    print("Какой тип сущности вы хотите просмотреть?")
    print("1. Пони")
    print("2. Единорог")
    print("3. Пегас\n")

    entity_choice = input("Ваш выбор: ")

    if entity_choice == '1':
        if len(ponies) > 0:
            for pony in ponies:
                print(pony)
        else:
            print("Список пони пуст.\n")
    elif entity_choice == '2':
        if len(unicorns) > 0:
            for unicorn in unicorns:
                print(unicorn)
        else:
            print("Список единорогов пуст.\n")
    elif entity_choice == '3':
        if len(pegasi) > 0:
            for pegasus in pegasi:
                print(pegasus)
        else:
            print("Список пегасов пуст.\n")
    else:
        print("Неверный выбор. Попробуйте снова.\n")
        view_entities()

def find_index(array,    attribute, value):
    for i in range(len(array)):
        if getattr(array[i], attribute) == value:
            return i
    return -1

def main_menu():
    print("\nВыберите действие:\n")
    print("1. Добавить сущность")
    print("2. Изменить сущность")
    print("3. Удалить сущность")
    print("4. Просмотреть список сущностей")
    print("5. Выход\n")

    choice = input("Ваш выбор: ")

    if choice == '1':
        add_entity()
    elif choice == '2':
        change_entity()
    elif choice == '3':
        delete_entity()
    elif choice == '4':
        view_entities()
    elif choice == '5':
        print("До свидания!")
        #return
        exit()
    else:
        print("Неверный выбор. Попробуйте снова.\n")
        main_menu()

##########

import unittest

class TestAddEntity(unittest.TestCase):
    def test_add_pony(self):
        ponies = []
        pony_data = {"name": "Sparkle", "age": 4}
        added_pony = Pony(**pony_data)
        ponies.append(added_pony)
        self.assertEqual(len(ponies), 1)
        self.assertEqual(ponies[0].name, "Sparkle")
        self.assertEqual(ponies[0].age, 4)

    def test_add_unicorn(self):
        unicorns = []
        unicorn_data = {"name": "Luna", "age": 100, "magic_power": True}
        added_unicorn = Unicorn(**unicorn_data)
        unicorns.append(added_unicorn)
        self.assertEqual(len(unicorns), 1)
        self.assertEqual(unicorns[0].name, "Luna")
        self.assertEqual(unicorns[0].age, 100)
        self.assertTrue(unicorns[0].magic_power)

    def test_add_pegasus(self):
        pegasi = []
        pegasus_data = {"name": "Cloudkicker", "age": 20, "can_fly": True}
        added_pegasus = Pegasus(**pegasus_data)
        pegasi.append(added_pegasus)
        self.assertEqual(len(pegasi), 1)
        self.assertEqual(pegasi[0].name, "Cloudkicker")
        self.assertEqual(pegasi[0].age, 20)
        self.assertTrue(pegasi[0].can_fly)

class TestDeleteEntity(unittest.TestCase):
    def setUp(self):
        self.ponies = [Pony("Sparkle", 4)]
        self.unicorns = [Unicorn("Luna", 100, True)]
        self.pegasi = [Pegasus("Cloudkicker", 20, True)]

    def test_delete_pony(self):
        ponies = self.ponies[:]
        ponies.pop(0)
        self.assertEqual(len(ponies), 0)

    def test_delete_unicorn(self):
        unicorns = self.unicorns[:]
        unicorns.pop(0)
        self.assertEqual(len(unicorns), 0)

    def test_delete_pegasus(self):
        pegasi = self.pegasi[:]
        pegasi.pop(0)
        self.assertEqual(len(pegasi), 0)

class TestChangeEntity(unittest.TestCase):
    def setUp(self):
        self.ponies = [Pony("Sparkle", 4)]
        self.unicorns = [Unicorn("Luna", 100, True)]
        self.pegasi = [Pegasus("Cloudkicker", 20, True)]

    def test_change_pony(self):
        self.ponies[0].name = "Twilight"
        self.ponies[0].age = 8
        self.assertEqual(self.ponies[0].name, "Twilight")
        self.assertEqual(self.ponies[0].age, 8)

    def test_change_unicorn(self):
        self.unicorns[0].name = "Nightmare Moon"
        self.unicorns[0].age = 50
        self.unicorns[0].magic_power = False
        self.assertEqual(self.unicorns[0].name, "Nightmare Moon")
        self.assertEqual(self.unicorns[0].age, 50)
        self.assertFalse(self.unicorns[0].magic_power)

    def test_change_pegasus(self):
        self.pegasi[0].name = "Storm"
        self.pegasi[0].age = 30
        self.pegasi[0].can_fly = False
        self.assertEqual(self.pegasi[0].name, "Storm")
        self.assertEqual(self.pegasi[0].age, 30)
        self.assertFalse(self.pegasi[0].can_fly)

if __name__ == '__main__':
    #while(True):
        #main_menu()
    unittest.main()


######
# Запуск программы


