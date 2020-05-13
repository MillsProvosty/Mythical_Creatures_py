from lib.hobbit import Hobbit

class TestHobbit:


    def test_it_has_a_name(self):
        hobbit = Hobbit("Bilbo")
        assert hobbit.name,"Bilbo"


    def test_it_is_named_something_else(self):
        hobbit = Hobbit("Pippin")
        assert hobbit.name, "Pippin"

    def test_disposition_is_unadventurous(self):
        hobbit = Hobbit("Samwise")
        assert hobbit.disposition, "homebody"


    def test_can_have_a_different_disposition(self):
        hobbit = Hobbit("Frodo", "adventurous")
        assert hobbit.disposition, "adventurous"

    def test_grows_older_when_celebrating_birthdays(self):
        hobbit = Hobbit('Merry')
        count = 0
        while count < 5:
            hobbit.celebrate_birthday()
            count += 1
        assert hobbit.age, 5

    def test_is_considered_a_child_at_32(self):
        hobbit = Hobbit('Hamfast')

        count = 0
        while count < 32:
            hobbit.celebrate_birthday()
            count += 1

        assert not hobbit.is_adult(), True

    def test_comes_of_age_at_33(self):
        hobbit = Hobbit('Lotho')
        count = 0
        while count < 35:
            hobbit.celebrate_birthday()
            count += 1

        assert hobbit.is_adult(), True


    def test_is_old_at_age_of_101(self):
        hobbit = Hobbit("Lobelia", "nosey")

        count = 0
        while count < 101:
            hobbit.celebrate_birthday()
            count += 1

        assert hobbit.is_old(), True

    def test_hobbit_has_the_ring_if_its_name_is_frodo(self):
        frodo = Hobbit("Frodo", "Brave")
        samwise = Hobbit("Samwise", "Supportive")

        assert frodo.has_ring(), True
        assert not samwise.has_ring(), True


    def test_hobbits_are_short(self):
        hobbit = Hobbit("Old Toby")

        assert hobbit.is_short, True

