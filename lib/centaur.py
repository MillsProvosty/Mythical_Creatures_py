class Centaur:

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        self.is_cranky = False
        self.is_standing = True
        self.mood_count = 0
        self.is_laying = False

    def run(self):
        if self.is_cranky:
            return "NO!"
        else:
            self.mood_count += 1
            return "Clip clop clip clop"

    def shoot(self):
        self.mood_count += 1
        if self.lay_down():
            return "NO!"
        elif self.mood_count == 3:
            self.is_cranky = True
            return "NO!"
        else:
            return "Twang!!!"

    def sleep(self):
        if self.is_standing:
            return "NO!"
        else:
            self.is_cranky = False
            self.mood_count = 0
            return "Zzzzzz"

    def lay_down(self):
        self.is_standing = False
        self.is_laying = True

    def stand_up(self):
        self.is_standing = True
        self.is_laying = False

    def drinks_potion(self):
        if not self.is_cranky:
            return "*HURL*"
        elif self.is_laying:
            return "NO!"
        else:
            self.mood_count = 0
            self.is_cranky = False
