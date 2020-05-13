class Hobbit:


    def __init__(self, name, disposition = "homebody"):
        self.name = name
        self.disposition = disposition
        self.is_short = True
        self.age = 0

    def celebrate_birthday(self):
        self.age += 1

    def is_adult(self):
        if self.age < 33:
            return False
        else:
            return True

    def is_old(self):
        if self.age < 101:
            return False
        else:
            return True

    def has_ring(self):
        if self.name == "Frodo":
            return True
