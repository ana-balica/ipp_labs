from lab2.main import CSV, ControlMainWindow, PriceCalculator


class TestPriceCalculator(object):
    def setup_method(self, method):
        csv = CSV('pricelist.csv')
        self.ingredients = csv.load_ingredients()
        self.price_calc = PriceCalculator(self.ingredients)

    def test_compute_price(self):
        assert self.price_calc.compute_price([]) == 0

        ingredients = ["Prosciutto", "Rucola", "Dor Blue"]
        price = self.price_calc.compute_price(ingredients)
        assert price == 162

        ingredients.append("Not in the pricelist")
        price = self.price_calc.compute_price(ingredients)
        assert price == 162
