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
        self.pizza_app.toggle_order_button()
        assert self.pizza_app.ui.order_btn.isEnabled() is False

        self.pizza_app.ui.order_btn.setText("some text")
        self.pizza_app.toggle_order_button()
        assert self.pizza_app.ui.order_btn.isEnabled() is False

        self.pizza_app.ui.name_input.setText("")
        self.pizza_app.ui.ch_bacon.setChecked(True)
        self.pizza_app.toggle_order_button()
        assert self.pizza_app.ui.order_btn.isEnabled() is False

        self.pizza_app.ui.name_input.setText("some text")
        self.pizza_app.toggle_order_button()
        assert self.pizza_app.ui.order_btn.isEnabled() is True

