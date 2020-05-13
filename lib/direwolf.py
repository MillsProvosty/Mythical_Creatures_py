from lib.stark import Stark


class Direwolf:

    def __init__(self, name, home, size):
        self.name = name
        self.home = home
        self.size = size
        self.starks_to_protect = []
        self.protected_stark_count = 0

    def protects(self, name):
        if self.protected_stark_count <= 2:
            self.starks_to_protect.append(name)

    def hunts_white_walkers(self):
        self.protected_stark_count = 0

    def leaves(self, name):
        name.safe = False
        self.starks_to_protect.remove(name)
