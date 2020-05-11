from lib.centaur import Centaur
class TestCentaur:
    def test_run(self):
        centaur = Centaur("Bob", "Pony")
        assert centaur.run(), "Clip clop clip clop"

    def test_shoot(self):
        centaur = Centaur("Bob", "Pony")
        assert centaur.shoot(), "Twang!!!"
