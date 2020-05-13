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

    def test_not_cranky(self):
        centaur = Centaur("George", "Palomino")
        assert centaur.is_cranky, False

    def test_standing_when_created(self):
        centaur = Centaur("George", "Palomino")
        assert centaur.is_standing, True

    def test_cranky_after_three_bow_shoot(self):
        centaur = Centaur("George", "Palomino")

        assert centaur.is_cranky, False
        centaur.shoot
        centaur.shoot
        centaur.shoot
        assert centaur.is_cranky, True

    def test_when_cranky_it_will_not_shoot_a_bow(self):
        centaur = Centaur("George", "Palomino")
        centaur.shoot
        centaur.shoot
        centaur.shoot
        assert centaur.shoot, "No"



    def test_when_cranky_it_will_not_run(self):
        centaur = Centaur("George", "Palomino")
        centaur.shoot
        centaur.shoot
        centaur.shoot
        assert centaur.run, "NO!"


    def test_when_standing_it_will_not_sleep(self):
        centaur = Centaur("George", "Palomino")
        assert centaur.sleep, "NO!"


    def test_after_laying_down_it_is_not_standing(self):
        centaur = Centaur("George", "Palomino")
        centaur.lay_down
        assert centaur.is_standing, False
        assert centaur.is_laying, True

    def test_it_can_sleep_when_laying_down(self):
        centaur = Centaur("George", "Palomino")
        centaur.lay_down
        assert not centaur.sleep, "NO!"
        assert centaur.sleep, "Zzzzzzz"


    def test_when_laying_down_it_cannot_shoot_a_bow
        centaur = Centaur("George", "Palomino")
        centaur.lay_down
        assert centaur.shoot, "NO!"


    def test_when_laying_down_it_cannot_run
        centaur = Centaur("George", "Palomino")
        centaur.lay_down
        assert centaur.run, "NO!"


    def test_it_can_stand_up
        centaur = Centaur("George", "Palomino")
        centaur.lay_down
        centaur.stand_up
        assert centaur.is_standing, True

    def test_after_sleeping_it_is_no_longer_cranky
        centaur = Centaur("George", "Palomino")

        centaur.shoot
        centaur.run
        centaur.shoot

        assert centaur.is_cranky, True

        centaur.lay_down
        centaur.sleep

        assert centaur.is_cranky, False

        centaur.stand_up

        assert centaur.shoot, "Twang!!!"
        assert centaur.run, "Clip clop clip clop"

    def test_becomes_rested_after_drinking_a_potion(self):
        centaur = Centaur("George", "Palomino")
        centaur.shoot
        centaur.run
        centaur.shoot
        centaur.drinks_potion
        assert centaur.is_cranky, False

    def test_can_only_drink_potion_while_standing(self):
        centaur = Centaur("George", "Palomino")
        centaur.lay_down
        assert centaur.drinks_potion, False

    def test_gets_sick_if_drinks_potion_while_rested(self):
        centaur = Centaur("George", "Palomino")
        centaur.lay_down
        centaur.sleep
        centaur.stand_up
        assert centaur.drinks_potion, "*HURL*"