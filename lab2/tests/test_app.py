import sys
from PySide import QtGui

from lab2.main import CSV, ControlMainWindow, PriceCalculator


class TestPizzaApp(object):
    qapplication = False

    def setup_method(self, method):
        csv = CSV('pricelist.csv')
        self.ingredients = csv.load_ingredients()
        if not TestPizzaApp.qapplication:
            self.app = QtGui.QApplication(sys.argv)
            TestPizzaApp.qapplication = True
        self.pizza_app = ControlMainWindow(self.ingredients)


    def test_toggle_order_button(self):
        assert self.pizza_app.ui.order_btn.isEnabled() is False

        self.pizza_app.ui.order_btn.setText("some text")
        assert self.pizza_app.ui.order_btn.isEnabled() is False

        self.pizza_app.ui.name_input.setText("")
        self.pizza_app.ui.ch_bacon.setChecked(True)
        assert self.pizza_app.ui.order_btn.isEnabled() is False

        self.pizza_app.ui.name_input.setText("some text")
        assert self.pizza_app.ui.order_btn.isEnabled() is True

    def test_update_price(self):
        assert self.pizza_app.ui.price_label.text() == u"Price: 00 lei"
        self.pizza_app.ui.ch_bacon.setChecked(True)
        assert self.pizza_app.ui.price_label.text() == u"Price: 100 lei"
        self.pizza_app.ui.ch_feta.setChecked(True)
        assert self.pizza_app.ui.price_label.text() == u"Price: 120 lei"
        self.pizza_app.ui.ch_bacon.setChecked(False)
        assert self.pizza_app.ui.price_label.text() == u"Price: 20 lei"

    def test_update_pizza_contents(self):
        assert self.pizza_app.ui.pizza_contents.text() == u"Your pizza contains:"
        self.pizza_app.ui.ch_bacon.setChecked(True)
        assert self.pizza_app.ui.pizza_contents.text() == u"Your pizza contains: Bacon."
        self.pizza_app.ui.ch_bacon.setChecked(False)
        assert self.pizza_app.ui.pizza_contents.text() == u"Your pizza contains:"

        self.pizza_app.ui.ch_ham.setChecked(True)
        self.pizza_app.ui.ch_smoked_mushrooms.setChecked(True)
        assert self.pizza_app.ui.pizza_contents.text() == u"Your pizza contains: Ham, Smoked mushrooms."
