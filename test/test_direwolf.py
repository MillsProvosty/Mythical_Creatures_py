from lib.direwolf import Direwolf
from lib.stark import Stark


class TestDirewolf:
    def test_direwolf_has_a_name(self):
        wolf = Direwolf('Nymeria')

        assert wolf.name, 'Nymeria'

    def test_default_home_is_beyond_the_wall_and_can_have_another_name(self):
        wolf = Direwolf('Lady')

        assert wolf.home, 'Beyond the Wall'
        assert wolf.name, 'Lady'

    def test_default_size_is_massive(self):
        wolf = Direwolf('Ghost')

        assert wolf.size, 'Massive'
        assert wolf.name, 'Ghost'

    def test_can_have_another_home_or_size(self):
        wolf = Direwolf('Shaggydog', "Winterfell", "Smol Pupper")

        assert wolf.name, "Shaggydog"
        assert wolf.home, 'Winterfell'
        assert wolf.size, "Smol Pupper"

    def test_starks_are_in_winterfell_by_default(self):
        wolf = Direwolf('Summer', 'Winterfell')
        stark = Stark('Bran')

        assert wolf.home, 'Winterfell'
        assert stark.location, 'Winterfell'

    def test_starts_off_with_no_Starks_to_protect(self):
        wolf = Direwolf('Nymeria')
        stark = Stark('Arya')

        assert stark.name, 'Arya'
        assert stark.location, 'Winterfell'
        assert wolf.home, 'Beyond the Wall'

    def test_protects_stark_kids(self):
        wolf = Direwolf('Nymeria', 'Riverlands')
        stark = Stark('Arya', 'Riverlands')

        wolf.protects(stark)

        assert wolf.starks_to_protect[0], 'Arya'
        assert stark.location, 'Riverlands'
        assert wolf.home, 'Riverlands'

    def test_can_only_protect_stark_kids_if_home_and_location_match(self):
        wolf = Direwolf('Ghost')
        stark = Stark('John', "King's Landing")

        wolf.protects(stark)

        assert wolf.starks_to_protect, []
        assert wolf.home, 'Beyond the Wall'

    def test_direwolf_can_only_protect_two_starks_at_a_time(self):
        summer_wolf = Direwolf('Summer', "Winterfell")
        lady_wolf = Direwolf('Lady', "Winterfell")
        sansa_stark = Stark('Sansa')
        john_stark = Stark('John')
        rob_stark = Stark('Rob')
        bran_stark = Stark('Bran')
        arya_stark = Stark('Arya')

        summer_wolf.protects(sansa_stark)
        summer_wolf.protects(john_stark)
        lady_wolf.protects(rob_stark)
        lady_wolf.protects(bran_stark)
        lady_wolf.protects(arya_stark)

        summer_num = len(summer_wolf.starks_to_protect)
        lady_num = len(lady_wolf.starks_to_protect)
        assert summer_num, 2
        assert lady_num, 2


    def test_starks_start_off_unsafe(self):
        stark = Stark('John', "The Wall")

        assert not stark.safe
        assert stark.house_words, 'Winter is Coming'

    def test_protected_status_changes_once_protected(self):
        wolf = Direwolf('Nymeria', "Winterfell")
        arya_stark = Stark('Arya')
        sansa_stark = Stark('Sansa')

        wolf.protects(arya_stark)

        assert arya_stark.safe, True
        assert arya_stark.house_words, 'The North Remembers'
        assert sansa_stark.house_words, 'Winter is Coming'

    def test_hunts_white_walkers(self):
        wolf = Direwolf('Nymeria', "Winterfell")

        assert wolf.hunts_white_walkers

    def test_hunts_white_walkers_but_not_if_protecting_starks(self):
        wolf = Direwolf('Nymeria', "Winterfell")
        stark = Stark('Sansa')

        wolf.protects(stark)

        wolf.hunts_white_walkers()

    def test_wolves_can_leave_and_stop_protecting_starks(self):
        summer_wolf = Direwolf('Summer', "Winterfell")
        lady_wolf = Direwolf('Lady', "Winterfell")
        sansa_stark = Stark('Sansa')
        arya_stark = Stark('Arya')

        summer_wolf.protects(arya_stark)
        lady_wolf.protects(sansa_stark)
        summer_wolf.leaves(arya_stark)

        assert summer_wolf.starks_to_protect, []
        assert lady_wolf.starks_to_protect, [sansa_stark]
        assert not arya_stark.safe, True

    def test_if_stark_not_protected_when_direwolf_leaves_then_that_stark_is_the_return_value(self):
        summer_wolf = Direwolf('Summer', "Winterfell")
        lady_wolf = Direwolf('Lady', "Winterfell")
        sansa_stark = Stark('Sansa')
        arya_stark = Stark('Arya')
        rickon_stark = Stark('Rickon')

        summer_wolf.protects(arya_stark)
        lady_wolf.protects(sansa_stark)
        lady_wolf.protects(rickon_stark)
        summer_wolf.leaves(arya_stark)
        lady_wolf.leaves(rickon_stark)

        assert not arya_stark.safe, True
        assert summer_wolf.leaves(arya_stark), "Arya"
