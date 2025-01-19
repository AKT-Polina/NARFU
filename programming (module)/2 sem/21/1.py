class pony:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print("Пони ", self.name, " бежит")

    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age
        
if __name__ == "__main__":
    p = pony("Рарити", 22)
    p.run()
    print(p.get_name())
    p.set_name("Пинкипай")
    print(p.get_name())
    print(p.get_age())
    p.set_age(10)
    print(p.get_age())
