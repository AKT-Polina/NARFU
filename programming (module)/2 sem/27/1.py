import time
import functools
#Подсчет времени
def time_of_function(function):
    def wrapped(*args):
        start_time = time.perf_counter_ns()
        res = function(*args)
        print(time.perf_counter_ns() - start_time)
        return res
    return wrapped
#Подсчет сколько раз вызвали
def counter(fu):
    
    def inner(*a,**kw):
        inner.count+=1
        return fu(*a,**kw)
    inner.count = 0
    return inner


class Pony:
    def __init__(self, name="Noname", age=0, price=100):
        self.name = name
        self.age = age
        self.price = price

    def __repr__(self):
        return f"Pony({self.name!r}, {self.age}, {self.price})"

class Shop:
   
    def __init__(self, ponies=None):
        if ponies is None:
            ponies = []
        self.ponies = ponies

    @counter
    @time_of_function
    def add_pony(self, pony):
        self.ponies.append(pony)


    def remove_pony(self, pony):
        if pony in self.ponies:
            self.ponies.remove(pony)

    def get_total_value(self):
        total_value = sum([pony.price for pony in self.ponies])
        return total_value

    def __repr__(self):
        return f"Shop({self.ponies!r})"

# Пример использования
sparkle = Pony("Sparkle", 4, 150)
twilight = Pony("Twilight", 8, 200)

shop = Shop()
shop.add_pony(sparkle)
shop.add_pony(twilight)

print(shop)
print(shop.get_total_value())
print(shop.add_pony.count)
