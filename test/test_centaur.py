from lib.centaur import Centaur
class TestCentaur:
    def test_run(self):
        centaur = Centaur("Bob", "Pony")
        assert centaur.run(), "Clip clop clip clop"

    def test_shoot(self):
        centaur = Centaur("Bob", "Pony")
        assert centaur.shoot(), "Twang!!!"

    def test_name(self):
        centaur = Centaur("Bob", "Pony")
        assert centaur.name, "Bob"

    def test_breed(self):
        centaur = Centaur("Bob", "Pony")
        assert centaur.breed, "Pony"