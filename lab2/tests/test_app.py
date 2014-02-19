import sys
from PySide import QtGui

from lab2.main import CSV, ControlMainWindow, PriceCalculator


class TestPizzaApp(object):
    def setup_method(self, method):
        csv = CSV('pricelist.csv')
        self.ingredients = csv.load_ingredients()
        self.price_calc = PriceCalculator(self.ingredients)
        app = QtGui.QApplication(sys.argv)
        self.app = ControlMainWindow()

    def test_compute_price(self):
        assert self.price_calc.compute_price([]) == 0

        ingredients = ["Prosciutto", "Rucola", "Dor Blue"]
        price = self.price_calc.compute_price(ingredients)
        assert price == 162

        ingredients.append("Not in the pricelist")
        price = self.price_calc.compute_price(ingredients)
        assert price == 162