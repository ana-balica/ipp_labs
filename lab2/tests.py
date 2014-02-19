from main import CSV


class TestCSV(object):
    def setup_method(self, method):
        self.csv = CSV('pricelist.csv')

    def test_load_ingredients(self):
        data = self.csv.load_ingredients()
        assert data["bacon"] == 100
        assert data["chili_pepper"] == 33
