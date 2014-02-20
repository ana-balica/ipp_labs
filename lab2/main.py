import sys
import random
from csv import reader

from PySide import QtGui, QtCore
from pizza_ui import Ui_MainWindow


MAX_CHEESE_ING = 3
MAX_MEAT_ING = 2
MAX_VEGETABLES_ING = 5


class CSV(object):
    """ CSV class for loading ingredients data.

    Can be extended to write new data, update data, etc
    """
    def __init__(self, filename):
        """ Initializer

        @param filename: valid path to a valid CSV file
        """
        self.filename = filename

    def load_ingredients(self):
        """ Load data about ingredients from CSV

        @rtype: dictionary
        @return: key/value of ingredients' names and their prices
        """
        data = {}
        with open(self.filename, 'rb') as csvfile:
            f = reader(csvfile, delimiter=',')
            for row in f:
                data[row[0]] = int(row[1])
        return data


class PriceCalculator(object):
    """ Simple price calculator
    """
    def __init__(self, pricelist):
        """ Initializer

        @param pricelist: a dictionary of ingredient names and prices
        """
        self.pricelist = pricelist

    def compute_price(self, ingredients):
        """ Sum up the price for all ingredients

        @param ingredients: list of ingredients
        @return: int price
        """
        price = 0
        for ingredient in ingredients:
            if self.pricelist.get(ingredient):
                price += self.pricelist[ingredient]
        return price


class ControlMainWindow(QtGui.QMainWindow):
    """ Main control window of the application

    """
    def __init__(self, ingredients, parent=None):
        """ Initialiser, calls binding to such elements as buttons, checkboxes

        :param ingredients: a dictionary of ingredient names and prices
        """
        super(ControlMainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.bind_ingredients()
        self.bind_name_input()
        self.bind_order_btn()

        self.ingredients = ingredients
        self.selected_ingredients = []

    def bind_ingredients(self):
        """ Bind all checkboxes that represent ingredients on changed state to
        several actions

        """
        for element in self.ui.centralwidget.findChildren(QtGui.QCheckBox):
            element.stateChanged.connect(self.update_pizza_contents)
            element.stateChanged.connect(self.update_price)
            element.stateChanged.connect(self.toggle_order_button)
            element.stateChanged.connect(self.check_ingredients)

    def update_pizza_contents(self, state):
        """ Update the multiline text label with ingredients selected

        :param state: state of the checkbox: checked/unchecked
        """
        sender = self.sender()
        if state == QtCore.Qt.Checked:
            self.selected_ingredients.extend([sender.text()])
        else:
            self.selected_ingredients.remove(sender.text())
        self.ui.pizza_contents.setText("Your pizza contains:")
        for ingredient in self.selected_ingredients:
            full_text = self.ui.pizza_contents.text()
            if full_text.endswith(':'):
                self.ui.pizza_contents.setText(full_text + " " + ingredient + ".")
            else:
                self.ui.pizza_contents.setText(full_text[:-1] + ", " + ingredient + ".")

    def update_price(self):
        """ Update the price text label with the total pizza price
        """
        price_calc = PriceCalculator(self.ingredients)
        price = price_calc.compute_price(self.selected_ingredients)
        self.ui.price_label.setText("Price: {0} lei".format(price))

    def check_ingredients(self):
        """ Control the number of selected ingredients, each group has a max value
        allowed to be added to pizza. If max number is reached, disable the rest
        of the checkboxes in the group.
        """
        cheese_count = 0
        cheese_ingredients = self.ui.widget3.findChildren(QtGui.QCheckBox)
        for cheese in cheese_ingredients:
            if cheese.isChecked():
                cheese_count += 1
            if cheese_count >= MAX_CHEESE_ING:
                for cheese in cheese_ingredients:
                    if not cheese.isChecked():
                        cheese.setEnabled(False)
            else:
                for cheese in cheese_ingredients:
                    cheese.setEnabled(True)

        meat_count = 0
        meat_ingredients = self.ui.widget1.findChildren(QtGui.QCheckBox)
        for meat in meat_ingredients:
            if meat.isChecked():
                meat_count += 1
            if meat_count >= MAX_MEAT_ING:
                for meat in meat_ingredients:
                    if not meat.isChecked():
                        meat.setEnabled(False)
            else:
                for meat in meat_ingredients:
                    meat.setEnabled(True)

        vegetables_count = 0
        vegetables_ingredients = self.ui.widget2.findChildren(QtGui.QCheckBox)
        for vegetable in vegetables_ingredients:
            if vegetable.isChecked():
                vegetables_count += 1
            if vegetables_count >= MAX_VEGETABLES_ING:
                for vegetable in vegetables_ingredients:
                    if not vegetable.isChecked():
                        vegetable.setEnabled(False)
            else:
                for vegetable in vegetables_ingredients:
                    vegetable.setEnabled(True)

    def bind_name_input(self):
        """ Bind name input to control the enabling of order button
        """
        self.ui.name_input.textChanged.connect(self.toggle_order_button)

    def toggle_order_button(self):
        """ Enable/disable order button if name input contains any text and if
        at least one ingredient is selected
        """
        text = self.ui.name_input.text()
        if text:
            state_input = True
        else:
            state_input = False
        state_checkbox = False
        for element in self.ui.centralwidget.findChildren(QtGui.QCheckBox):
            if element.isChecked():
                state_checkbox = True
                break
        self.ui.order_btn.setEnabled(state_input and state_checkbox)

    def bind_order_btn(self):
        """ Bind order button to finish order action
        """
        self.ui.order_btn.clicked.connect(self.finish_order)

    def finish_order(self):
        """ Finish the order by displaying a message box with order id
        """
        name = self.ui.name_input.text()
        short_id = random.randint(1, 999)
        msg = QtGui.QMessageBox()
        msg.setText("Thank you {0}!\nYour order ID is {1}.".format(name, short_id))
        msg.exec_()


if __name__ == "__main__":
    csv = CSV('pricelist.csv')
    ingredients = csv.load_ingredients()
    app = QtGui.QApplication(sys.argv)
    pizza_app = ControlMainWindow(ingredients)
    pizza_app.show()
    sys.exit(app.exec_())
