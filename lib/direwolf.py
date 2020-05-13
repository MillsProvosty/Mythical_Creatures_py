
class Direwolf:

    def __init__(self, name, home = "The North", size = "Big"):
        self.name = name
        self.home = home
        self.size = size
        self.starks_to_protect = []


    def protects(self, stark):
        while len(self.starks_to_protect) <= 1:
            stark.safe = True
            self.starks_to_protect.append(stark)

    def hunts_white_walkers(self):
        self.starks_to_protect = []

    def leaves(self, name):
        name.safe = False
        return name.name

