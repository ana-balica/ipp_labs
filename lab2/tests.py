import pytest

from main import CSV


class TestCSV(object):
    def setup_method(self, method):
        self.csv = CSV('pricelist.csv')

    def test_load_ingredients(self):
        data = self.csv.load_ingredients()
        assert data["Bacon"] == 100
        assert data["Chili pepper"] == 33
        with pytest.raises(KeyError):
            data["some_other_ingredient"]
