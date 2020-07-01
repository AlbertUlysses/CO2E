import pytest
from beagreenie.beagreenie import fuel_combustion


class TestFuelCombustion(object):

    def test_fuel_combustion(self):
        test = fuel_combustion(32)
        assert test == 275

