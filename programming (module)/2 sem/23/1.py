from datetime import datetime
import pickle
import unittest
import gc

class testPony(unittest.TestCase):

    def setUp(self):
        self.p = pony("Sparkle")

    def tearDown(self):
        del self.p

    def test_destructor(self):
        # Сбрасываем счетчик ссылок вручную, чтобы принудительно вызвать сборку мусора
        gc.collect()
        # Проверяем, что _is_deleted стало True после удаления объекта
        self.assertTrue(self.p._is_deleted)


class persistence_pony(object):
    @staticmethod
    def serialize(pony):
        with open('ponyes.pkl', 'wb') as f:
            pickle.dump(pony, f)
        f.closed
    @staticmethod
    def deserialize():
        with open('ponyes.pkl', 'rb') as f:
            account = pickle.load(f)
        f.closed
        return account

class transaction:

    def __init__(self, event):
        self.when = datetime.today()
        self.event = event

class pony:
    
    def __init__(self, name="Noname", age=0):
        self.name = name
        self.age = age
        self.queue = []
        self._is_deleted = False


    def get_events(self):
        for i in self.queue:
            print(i.when, " ", i.event)
    
    def __del__(self):
        self._is_deleted = True
        print(f"Пони {self.name} был удален.")
        
    def __str__(self):
        return 'Имя: {0}, Возраст: {1}'.format(self.name, self.age)

    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age

    def set_name(self, name):
        self.queue.append(transaction("Изменение имени: было " + self.name+ " стало " + name))
        self.name = name

    def set_age(self, age):
        self.queue.append(transaction("Изменение возраста: было " + str(self.age) + " стало " + str(age)))
        self.age = age
        
if __name__ == "__main__":
    p1 = pony("Рарити", 22)
    p1.set_name("Пинкипай")
    p1.set_name("Пинкипай")
    p1.set_age(12)
    p1.get_events()
    unittest.main()
    persistence_pony.serialize(p1)
    persistence_pony.deserialize()
    del p1
  
    
    

