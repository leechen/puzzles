from python.carFleets import Solution


def test_car_fleet_standard_example():
    assert Solution().carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]) == 3


def test_car_fleet_merges_cars_arriving_together():
    assert Solution().carFleet(10, [6, 8], [2, 1]) == 1


def test_car_fleet_with_no_cars():
    assert Solution().carFleet(10, [], []) == 0
